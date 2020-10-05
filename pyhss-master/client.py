#Interactive Diameter Client
import socket
import sys
import diameter
global recv_ip
#recv_ip = "10.0.1.252"
recv_ip = "127.0.0.1"  #client ip address
#hostname = input("Host to connect to:\t")
#domain = input("Domain:\t")

#hostname = "10.0.1.252"
hostname = "127.0.0.1"  #ip of hss diameter server
realm = "mnc001.mcc001.3gppnetwork.org"

supported_calls = ["CER", "DWR", "AIR", "ULR", "UAR", "PUR", "SAR", "MAR", "MCR", "LIR"]
'''
https://en.wikipedia.org/wiki/Diameter_(protocol)#Packet_Format
Capabilities-Exchange-Request	CER	257	Diameter base	CER
Device-Watchdog-Request	DWR	280	Diameter base	DWR
User-Authorization-Request	UAR	283	Diameter SIP Application - RFC 4740	UAR
Server-Assignment-Request	SAR	284	Diameter SIP Application - RFC 4740	SAR
Location-Info-Request	LIR	285	Diameter SIP Application - RFC 4740	LIR
Multimedia-Auth-Request	MAR	286	Diameter SIP Application - RFC 4740	MAR
User-Authorization-Request	UAR	300	Diameter base (3GPP) RFC 3589	UAR
Server-Assignment-Request	SAR	301	Diameter base (3GPP) RFC 3589	SAR
Location-Info-Request	LIR	302	Diameter base (3GPP) RFC 3589	LIR
Multimedia-Auth-Request	MAR	303	Diameter base (3GPP) RFC 3589	MAR
Profile-Update-Request	PUR	307	Diameter base (3GPP) RFC 3589	PUR
Update-Location-Request	ULR	316	3GPP TS 29.272 [RFC 5516]	ULR
Authentication-Information-Request	AIR	318	3GPP TS 29.272 [RFC 5516]	AIR


'''
#diameter = diameter.Diameter('nick-pc', 'mnc001.mcc001.3gppnetwork.org', 'PyHSS-client')
diameter = diameter.Diameter('localhost', 'mnc001.mcc001.3gppnetwork.org', 'PyHSS-client')

clientsocket = socket.socket()
print("Connecting to " + str(hostname))
try:
    clientsocket.connect((hostname,3868))
except Exception as e:
    print("Failed to connect to server - Error: " + str(e))
    sys.exit()


def ReadBuffer():
    try:
        data = clientsocket.recv(32)
        packet_length = diameter.decode_diameter_packet_length(data)            #Calculate length of packet from start of packet
        data_sum = data + clientsocket.recv(packet_length - 32)                 #Recieve remainder of packet from buffer
        packet_vars, avps = diameter.decode_diameter_packet(data_sum)  #and a Dict containing the packet variables (called *packet_vars*), Returns AVPs as an array, called *avp*
        print("Got response from " + str(hostname))
        for keys in packet_vars:
            print("\t" + str(keys) + "\t" + str(packet_vars[keys]))

        for avp in avps:
            print(avp['avp_code'])
            if int(avp['avp_code']) == 318:
                print("Received Authentication Information Answer - Store output of Crypto vectors?")
                file.open("vectors.txt", "w")
                file.write(avp['misc_data'])
                file.close()
        print("Command Code: " + str(packet_vars['command_code']))
        if int(packet_vars['command_code']) == 280:
            print("Recieved DWR - Sending DWA")
            SendRequest(diameter.Answer_280(packet_vars, avps))
        if int(packet_vars['command_code']) == 257:
            print("Recieved CER - Sending CEA")
            SendRequest(diameter.Answer_257(packet_vars, avps, recv_ip))
            
        if input("Print AVPs (Y/N):\t") == "Y":
            for avp in avps:
                print("\t\t" + str(avp))
                
    except Exception as e:
        print("failed to get all return data - Error " + str(e))

def SendRequest(request):
    clientsocket.sendall(bytes.fromhex(request))
    #>>> sampleBytes = bytes.fromhex("01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f");
    #>>> sampleBytes
    #b'\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f'
    #>>> sampleBytes = bytes.fromhex("0102030405060708090a0b0c0d0e0f")
    #>>> sampleBytes
    #b'\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f'

    print("waiting responding from server .....")
    ReadBuffer()   #waiting responding from server 

while True:
    print("\n\nQuerying Diameter peer " + str(hostname) + " of domain " + str(realm))
    print("Note - You may need to exchange a CER before doing anything fun")
    #request = input("Enter request type:\t")
    request = input("Enter request type:")

    if request == "R":
        ReadBuffer()
    elif request == "CER":
        print("Sending Cabailites Exchange Request to " + str(hostname))
        #troubleshooting
        message = diameter.Request_257()
        print("message, Request_257:\n", message, type(message) )
        
        '''
		message= 
'0100011880000101000000001ec78840c4c88cc2000001084000000f6e69636b2d70630000000128400000256d6e633030312e6d63633030312e336770706e6574776f726b2e6f7267000000000001014000000e00017f00010100000000010a4000000c000000000000010d0000001450794853532d636c69656e740000010b4000000c000027d90000010440000020000001024000000c010000230000010a4000000c000028af0000010440000020000001024000000c010000160000010a4000000c000028af0000010440000020000001024000000c010000000000010a4000000c000028af000001024000000cffffffff000001094000000c0000159f000001094000000c000028af000001094000000c000032db'
        '''
        
        print("Start send request....---------------------")
        SendRequest(diameter.Request_257())
        print("Request sent-------------------------------")

    elif request == "DWR":
        print("Sending Device Watchdog Request to " + str(hostname))
        SendRequest(diameter.Request_280())
    elif request == "ULR":
        imsi = str(input("IMSI:\t"))
        print("Sending Update Location Request to " + str(hostname))
        SendRequest(diameter.Request_16777251_316(imsi))
    elif request == "AIR":
        imsi = str(input("IMSI:\t"))
        print("Sending Authentication Information Request to " + str(hostname))
        SendRequest(diameter.Request_16777251_318(imsi))
    elif request == "UAR":
        imsi = str(input("IMSI:\t"))
        domain = str(input("Domain:\t"))
        print("Sending User Authentication Request to " + str(hostname))
        SendRequest(diameter.Request_16777216_300(imsi, domain))
    elif request == "PUR":
        imsi = str(input("IMSI:\t"))
        print("Sending User Purge Request to " + str(hostname))
        SendRequest(diameter.Request_16777251_321(imsi))
    elif request == "SAR":
        imsi = str(input("IMSI:\t"))
        domain = str(input("Domain:\t"))
        print("Sending Server Assignment Request to " + str(hostname))
        SendRequest(diameter.Request_16777216_301(imsi, domain))
    elif request == "MAR":
        imsi = str(input("IMSI:\t"))
        domain = str(input("Domain:\t"))
        print("Sending Multimedia Authentication Request to " + str(hostname))
        SendRequest(diameter.Request_16777216_303(imsi, domain))
    elif request == "MCR":
        imsi = str(input("IMSI:\t"))
        imei = str(input("IMEI:\t"))
        software_version = str(input("ME Software Version:\t"))
        print("Sending ME-Identity-Check Request " + str(hostname))
        SendRequest(diameter.Request_16777252_324(imsi, imei, software_version))
    elif request == "RTR":
        imsi = str(input("IMSI:\t"))
        domain = str(input("Domain:\t"))
        print("Sending Registration Termination Request to " + str(hostname))
        SendRequest(diameter.Request_16777216_304(imsi, domain))
    elif request == "LIR":
        msisdn = str(input("MSISDN:\t"))
        sipaor = "sip:" + str(msisdn)
        print("Sending Location-Information Request to " + str(hostname))
        SendRequest(diameter.Request_16777216_285(sipaor))
    else:
        print("Invalid input, valid entries are:")
        for keys in supported_calls:
            print(keys)

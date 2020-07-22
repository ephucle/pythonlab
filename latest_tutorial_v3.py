from timer import Timer
from reader import feed
def main():
	"""Download and print the latest tutorial from Real Python"""
	t = Timer()
	t.start()
	#tic = time.perf_counter()    
	tutorial = feed.get_article(0)
	#toc = time.perf_counter()
	t.stop()
	
	#print(f"Downloaded the tutorial in {toc - tic:0.4f} seconds")
	print(tutorial)

if __name__ == "__main__":
    main()

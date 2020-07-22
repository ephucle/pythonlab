from mathematicians import *
from bs4 import BeautifulSoup
def get_names():
    """
    Downloads the page where the list of mathematicians is found
    and returns a list of strings, one per mathematician
    """
    url = 'http://www.fabpedigree.com/james/mathmen.htm'
    response = simple_get(url)

#<li> <a href="#Poincare">Henri Poincar&eacute;</a>
#<li> <a href="#Lagrange">Joseph-Louis Lagrange</a>
#<li> <a href="#Euclid">Euclid</a> <small> of Alexandria</small>
#<li> <a href="#Hilbert">David Hilbert</a>
#<li> <a href="#Leibniz">Gottfried W. Leibniz</a>

    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        names = set()
        for li in html.select('li'):
            for name in li.text.split('\n'):
                if len(name) > 0:
                    names.add(name.strip())
        return list(names)

    # Raise an exception if we failed to get any data from the url
    raise Exception('Error retrieving contents at {}'.format(url))


def get_hits_on_name(name):
    """
    Accepts a `name` of a mathematician and returns the number
    of hits that mathematician's Wikipedia page received in the 
    last 60 days, as an `int`
    """
	
	#                                <a href='https://tools.wmflabs.org/pageviews?project=en.wikipedia.org&amp;pages=Henri%20Poincar%C3%A9&amp;range=latest-60' target='_blank'>28,054</a>

    # url_root is a template string that is used to build a URL.
    #url_root = 'URL_REMOVED_SEE_NOTICE_AT_START_OF_ARTICLE'
    #url_root = 'https://xtools.wmflabs.org/articleinfo/en.wikipedia.org/Henri_Poincar%C3%A9'
    name = name.replace(" ", "%20")
    url_root = 'https://xtools.wmflabs.org/articleinfo/en.wikipedia.org/'
    url_root +=name
    #print (url_root.format(name))
    print (url_root)
    #response = simple_get(url_root.format(name))
    response = simple_get(url_root)
    if response is not None:
        html = BeautifulSoup(response, 'html.parser')

        hit_link = [a for a in html.select('a')
                    if a['href'].find('latest-60') > -1]

        if len(hit_link) > 0:
            # Strip commas
            link_text = hit_link[0].text.replace(',', '')
            try:
                # Convert to integer
                return int(link_text)
            except:
                log_error("couldn't parse {} as an `int`".format(link_text))

    log_error('No pageviews found for {}'.format(name))
    return None

if __name__ == '__main__':
    print('Getting the list of names....')
    names = get_names()
    print('... done.\n')

    results = []

    print('Getting stats for each name....')

    for name in names:
        try:
            hits = get_hits_on_name(name)
            if hits is None:
                hits = -1
            results.append((hits, name))
        except:
            results.append((-1, name))
            log_error('error encountered while processing '
                      '{}, skipping'.format(name))

    print('... done.\n')

    results.sort()
    results.reverse()

    if len(results) > 5:
        top_marks = results[:5]
    else:
        top_marks = results

    print('\nThe most popular mathematicians are:\n')
    for (mark, mathematician) in top_marks:
        print('{} with {} pageviews'.format(mathematician, mark))

    no_results = len([res for res in results if res[0] == -1])
    print('\nBut we did not find results for '
          '{} mathematicians on the list'.format(no_results))
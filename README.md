Functions using Alexa's Top Million domain list, found here:
http://s3.amazonaws.com/alexa-static/top-1m.csv.zip

Available functions:

    is_top_n(domain, n)   # Determins if domain is in the top n Alexa domains
		get_rank(domain)      # Get the placing of domain in Alexa (or None)
		get_domain(n)         # Get the domain at the given Alex rank

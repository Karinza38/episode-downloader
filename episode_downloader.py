import urllib
import os
import time

def getTitle(page):
	''' 
	Gets the Episode Title (text when we hover over episode name)
	This gives info about the size of the torrent under inspection
	'''
	start=page.find(" title=\"")
	if start== -1:
		return "No Title in the Page"
	else:
		end=page.find("\"",start+10)
	
	return page[start+8:end] 
	
	
def getNextRow(page):
	start=page.find("<td class=\"forum_thread_post\">")
	if start==-1:
		print "Khaali Lotaa"
		return ""
	end=page.find("<td class=\"forum_thread_post\">",start+1)
	if end!=-1:
		content=page[start:end]
	else :
		content=page[start:]
	return content

fail_count=1


while True:
	page=urllib.urlopen("http://eztv.it/shows/481/").read() #481- Games Of Thrones
	content=getNextRow(page)
	while content.find(" S02E07 ")!=-1:
			if getTitle(content).find("MB")!=-1:
						#print getTitle(content)
						link_start=content.find("<a href=\"http")
						link_end=content.find("\"",link_start+10)		#print content[link_start+9:link_end]
						command="rtorrent "+ content[link_start+9:link_end]
						print command
						os.system(command)
						break
			else:
				print content
				page=page[page.find("<td class=\"forum_thread_post\">")+1:]
				content=getNextRow(page)
								
	print fail_count
	print getTitle(content)
	fail_count=fail_count+1
	time.sleep(300)

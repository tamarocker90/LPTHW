from sys import exit
#Script, directory, date, jobs, grep = argv 
#
#print 'find -L /data/logs/%s -name "*%s*" | parallel -j%s -k \"zcat {} | grep -i %s"' % (
#	directory, date, jobs, grep)

print '\n'
print '*' * 60
print "Welcome To The Pointless CSIRC Find Command Tool (TPCFCT)!"
print '*' * 60

logType = raw_input(""" \nWhich type of log would you like to search?
1. Web
2. Email
3. DNS
4. ASA
5. PA
6. ERAP

>"""
)

#convert user input into actual log directory name
if logType == '1': 
	logType = 'web_proxy'
	
elif logType == '2':
	logType = 'email'
	
elif logType == '3':
	logType = 'dns'
	
elif logType == '4':
	logType = 'asa_logs'
	
elif logType == '5':
	logType = 'pa_logs'
	
elif logType == '6':
	logType = 'erap'
	
else: 
	print '\n'
	print '!' * 60
	print "\nPlease start over and make a valid selection!\n"
	print '!' * 60
	exit(0)
	
date = raw_input("\nPlease Enter the Date: (YYMMDD)\n>")
jobs = raw_input("\nPlease enter the number of jobs you would like to run: [1-16]/n>")
grep = raw_input("\nPlease enter a search string:\n>")
case = raw_input("\nWould you like to make your search case sensitive? (Y/N)")


print "\nPlease use the following command:\n"

#check for case sensitivity
if case == 'Y' or case == 'y':
	print '\nfind -L /data/logs/%s -name "*%s*" | parallel -j%s -k \"zcat {} | grep %s"\n' % (
		logType, date, jobs, grep)

else:
	print '\nfind -L /data/logs/%s -name "*%s*" | parallel -j%s -k \"zcat {} | grep -i %s"\n' % (
		logType, date, jobs, grep)
	
#os.walk
#os.path.walk

#    walk(top, topdown=True, onerror=None, followlinks=False)
#        Directory tree generator.
#
#       For each directory in the directory tree rooted at top (including top
#        itself, but excluding '.' and '..'), yields a 3-tuple
#
#            dirpath, dirnames, filenames
#
#        dirpath is a string, the path to the directory.  dirnames is a list of
#        the names of the subdirectories in dirpath (excluding '.' and '..').
#        filenames is a list of the names of the non-directory files in dirpath.
#        Note that the names in the lists are just names, with no path components.
#        To get a full path (which begins with top) to a file or directory in
#        dirpath, do os.path.join(dirpath, name).
#
#        If optional arg 'topdown' is true or not specified, the triple for a
#        directory is generated before the triples for any of its subdirectories
#        (directories are generated top down).  If topdown is false, the triple
#        for a directory is generated after the triples for all of its
#        subdirectories (directories are generated bottom up).
#
#        When topdown is true, the caller can modify the dirnames list in-place
#        (e.g., via del or slice assignment), and walk will only recurse into the
#        subdirectories whose names remain in dirnames; this can be used to prune
#        the search, or to impose a specific order of visiting.  Modifying
#        dirnames when topdown is false is ineffective, since the directories in
#        dirnames have already been generated by the time dirnames itself is
#        generated.
#
#        By default errors from the os.listdir() call are ignored.  If
#        optional arg 'onerror' is specified, it should be a function; it
#        will be called with one argument, an os.error instance.  It can
#        report the error to continue with the walk, or raise the exception
#        to abort the walk.  Note that the filename is available as the
#        filename attribute of the exception object.
#
#        By default, os.walk does not follow symbolic links to subdirectories on
#        systems that support them.  In order to get this functionality, set the
#        optional argument 'followlinks' to true.
#
#        Caution:  if you pass a relative pathname for top, don't change the
#        current working directory between resumptions of walk.  walk never
#        changes the current directory, and assumes that the client doesn't
#        either.
#
#        Example:
#
#        import os
#        from os.path import join, getsize
#        for root, dirs, files in os.walk('python/Lib/email'):
#            print root, "consumes",
#            print sum([getsize(join(root, name)) for name in files]),
#            print "bytes in", len(files), "non-directory files"
#            if 'CVS' in dirs:
#                dirs.remove('CVS')  # don't visit CVS directories
#
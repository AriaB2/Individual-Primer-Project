#! /bin/bash

# This is a little CGI program


###################################################################
# The following are environment variables that are available to you
#
# CONTENT_TYPE:      The MIME type of associated with the option body of the HTTP request.
# CONTENT_LENGTH:    The length of the query information.
# GATEWAT_INTERFACE: Currently CGI/1.1
# HTTP_HOST:         The name of the vhost of the server.  
# HTTP_USER_AGENT:   Information about the browser/client that made requested.
# QUERY_STRING:      The query string.
# REQUEST_METHOD:    The method used to make the request. The most common methods are GET and POST.
# REQUEST_URI:       The URI of the request
# SERVER_PROTOCOL:   Currently HTTP/1.1
# SCRIPT_FILENAME:   The full path to the CGI script.
# SCRIPT_NAME:       The name (i.e., URI) of the CGI script.
# SERVER_NAME:       The server's hostname or IP Address
# SERVER_PORT:       The port of the server


#      Added a content type and a blank line


echo "X-Cit-160: hello again Stranger!"
echo "Content-type: text/html"

echo ""
echo "Current FileName: ${SCRIPT_NAME}"
echo "Current Script: ${SCRIPT_FILENAME}"


if [ -n "${QUERY_STRING}" ] ; then 
/usr/bin/curl -s http://www.csun.edu/engineering-computer-science/computer-science
else
echo "No specified query string was entered"
/usr/bin/curl -s https://www.csun.edu/~steve/
fi

# Read the body -- if it is a post
while read _post_line ; do
  echo ${_post_line} ";loop"
done 
echo $_post_line




exit 0

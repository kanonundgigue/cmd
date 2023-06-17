import subprocess

def my_cmd(inputs=""):
    process = (
    	subprocess.Popen(inputs, 
	    stdout=subprocess.PIPE, shell=True)
	    .communicate()[0]).decode('utf-8')[:-1].split("\n")
    return process
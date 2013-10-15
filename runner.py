import os
import sys
import getopt
import subprocess
import commands
import time
import glob
import signal

def usage():
    print '''
py runner.py [option][value]...
-h or --help
-v or --verbosit="unitest errlog level"
-p or --path="case path"
-s or --send ="email send to"
-c or --copy="email copy to"
-o or --output="log output to"
-t or --timeout="Maximum excuting time for each case"
'''

def colorPrintMessage(color, msg):
    """
    return a message that printed with color

    :color - could choose 'r', 'g', 'b', 'y'
    :msg   - the content will be printed in color

    Usage:
        colorPrintMessage('r', 'red color message')
    """

    if color == 'r':
        fore = 31
    elif color == 'g':
        fore = 32
    elif color == 'b':
        fore = 36
    elif color == 'y':
        fore = 33
    else:
        fore = 37
    color = "\x1B[%d;%dm" % (1,fore)
    return "%s %s\x1B[0m" % (color,msg)

    
def execmd(cmd, timeout):
    r'''Execute cmd and return the stdout value back
    This function ignore the cmd checking. If you want to
    us some dangerous command such as rm, mv, please check
    it before using
    '''
    args = cmd
    proc = subprocess.Popen(args, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
    t_beginning = time.time()
    seconds_passed = 0
    retV = None
    pid = proc.pid
    while True:
        if proc.poll() is not None:
            retV = proc.communicate()[0]
            break
        seconds_passed = time.time() - t_beginning
        if timeout and seconds_passed > timeout:
            retV = proc.communicate()[0]
            return (1, retV+"\nExcuting commad [%s] timeout" % cmd)
        time.sleep(0.1)
    return (0, retV)
 
def writeTempLog(case, err):
    fd = open(case+'.tmplog', 'w')
    fd.write(err)
    fd.flush()
    fd.close()
    fd = open(case+'.tmplog')
    lines = fd.readlines()
    fd.close()
    fd = open(case+'.tmplog', 'w')
    for l in lines:
        l = l.replace('\r\n', '\n')
        s = l.find('\x1b')
        e = l.find('\r')
        if s > -1 and e > -1:
            l = l[0:s] + l[e+1:]
        l = l.replace('\r', ' ')
        fd.write(l.replace('\x1b[60G','').replace('\x1b[0;31m', '').replace('\x1b[0;32m', '').replace('\x1b[0;39m', '').replace('\x1b[1;32m', '').replace('\x1b[0m', ''))
    fd.close()

def runcase(path, python, results, timeout):
    case_path = os.path.abspath(path)
    if not case_path.endswith('.yaml'):
        return
    output = None
    errput = None
    tmp = None
    try:
            commands.getoutput('%s data2case.py %s' % (python, case_path))
            c_path, c_name = os.path.split(case_path)
            c_name = c_name.rstrip('.yaml')
            print 'CASE %s is running ......' % c_name 
            st, output= execmd('%s %s.py'%(python, case_path.split('.yaml')[0]), timeout)

            if output.startswith('F\n==============================================='):
                errput = output.split('\n||Test Case||')[0]
                output = output[len(errput):]
            elif output.find('F\n======================================================================') > 0:
                tmp_0 = output.split('F\n======================================================================')[1].split('----------------------------------------------------------------------\nRan')
                tmp_1 = '\n'.join(tmp_0[1].split('\n')[:3])
                tmp_2 = 'F\n======================================================================' + tmp_0[0]
                tmp_2 = tmp_2 + '----------------------------------------------------------------------\nRan' + tmp_1
                errput = tmp_2 + '\n'
                output = output.split('F\n======================================================================')[0] + '\n'.join(tmp_0[1].split('\n')[3:])
            elif output.find('E\n======================================================================') >= 0:
                tmp_0 = output.split('E\n======================================================================')[1].split('----------------------------------------------------------------------\nRan')
                tmp_1 = '\n'.join(tmp_0[1].split('\n')[:3])
                tmp_2 = 'E\n======================================================================' + tmp_0[0]
                tmp_2 = tmp_2 + '----------------------------------------------------------------------\nRan' + tmp_1
                errput = tmp_2 + '\n'
                output = output.split('E\n======================================================================')[0] + '\n'.join(tmp_0[1].split('\n')[3:])
            elif output.find('\n\nOK\n\n'):
                errput = output.split('\n||Test Case||')[0]
                output = output[len(errput):]
                 
            os.system('rm -f %s.py'%case_path.split('.yaml')[0])
            if st:
                results[c_name] = 'TimeOut'
                output = 'TimeOut: %s \n' % c_name + output
                output = '======================================================================\n' + output
                output += '\n' 
                print ''.join(['CASE %s ...... ', colorPrintMessage('y', 'TimeOut')]) % c_name
                writeTempLog(c_name, output + '\n')
            else:
                tmp = errput.split('\n')
                if tmp[-2] != 'OK':
                    tmp[2] = 'FAIL: %s' % c_name
                    results[c_name] = 'FAIL'
                    print ''.join(['CASE %s ...... ', colorPrintMessage('r', 'FAIL')]) % c_name
                    writeTempLog(c_name, output + '\n'.join(tmp[1:-5])+ '\n')
                else:
                    results[c_name] = 'PASS'
                    print ''.join(['CASE %s ...... ', colorPrintMessage('g', 'PASS')]) % c_name
    except:
        c_name = os.path.split(case_path)[1]
        results[c_name] = 'Exceptioned'
        print ''.join(['CASE %s ...... ', colorPrintMessage('y', 'Exceptioned')]) % c_name 
        if output and tmp:
            writeTempLog(c_name, output + '\n'.join(tmp[1:-5])+ '\n')

def dotest(path, python, results, timeout):
    if not os.path.exists(path):
        return
    if os.path.isdir(path):
        abs_path = os.path.abspath(path)
        for p in os.listdir(abs_path):
            dotest(os.path.join(abs_path,p), python, results, timeout)
    else:
        runcase(path, python, results, timeout)


def writeLog(fname, results, summary):
    fd = open(fname,'w')
    g = glob.glob('*.tmplog')
    n = [ a[:-7] for a in g]
    for n, s in results.items():
            fd.write('%s ...... %s\n' % (n,s))
    fd.write('\n')    
    fd.write(summary)
    fd.write('\n')    
    fd.close()
    for f in glob.glob('*.tmplog'):
        os.system('cat %s >> %s' %(f, fname))    
    
if __name__ == '__main__':
    fmt = "%Y%m%d%H%M%S"
    timestamp = time.strftime(fmt, time.localtime())
    transfile =  os.path.abspath("log/record_%s.log"%(timestamp))

    send = "wb-yinlu@taobao.com"
    copy = ""
    path =  os.path.abspath("case/new")
    timeout = 60

    opts, args = getopt.getopt(sys.argv[1:], "hp:v:s:o:c:t:",["help","path=","verbosity="])
    for op, value in opts:
        if op == '-p':
            path = value
        elif op == '-v':
            ver=value
        elif op == '-s':
            send=value
        elif op == '-c':
            copy =value
        elif op =='-o':
            transfile=value
        elif op == '-t':
            timeout = int(value)
        elif op == '-h':
            usage()
            sys.exit(1)
        else:
            pass
    
    python = commands.getoutput('which python2.7')
    if python.strip().lower().startswith('which'):
        print colorPrintMessage('r', 'python2.7 not installed')
        sys.exit(1)
    if len(glob.glob('*.tmplog')):
        os.system('rm *.tmplog')
    results = dict()
    print "Test beginning........"
    print
   
    dotest(path, python, results, timeout)
    totalFail = 0
    totalPass = 0
    exceptioned = 0
    timeouted = 0
    for v in results.values():
        if v == 'FAIL':
            totalFail += 1
        elif v == 'PASS':
            totalPass += 1
        elif v == 'Exceptioned':
            exceptioned += 1
        else:
            timeouted += 1

    summary = "Total: %d\tPassed: %d\tFailed: %d\tTimeOut: %d\tExceptioned: %d" %(len(results), totalPass, totalFail, timeouted, exceptioned)
    print colorPrintMessage('y', summary)
    writeLog(transfile, results, summary)
    os.system('rm *.tmplog')
    cmd = "mailx -s 'rfc2616Case daily run' -r 'macaron' -c '%s' '%s' < %s"%(copy,send,transfile)
    commands.getoutput(cmd)

'''Start iKVM to remote access server using IPMI protocol'''

import argparse
import os

def launch_kvm(args):
    smcipmitool_dir = os.path.dirname(__file__)
    cmd = [
        os.path.join(args.jvm, 'bin/java'),
        '-Djava.library.path=' + smcipmitool_dir,
        '-jar', os.path.join(smcipmitool_dir, 'iKVM.jar'),
        args.host, args.user, args.password,
        # Not sure what exactly these paramaters mean, but that's what
        # used by SMCIPMITool kvm
        'null', '5900', '600', '0', '0'
    ]
    os.execv(cmd[0], cmd)

def main():
    parser = argparse.ArgumentParser(
        description = __doc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument('--user', default='ADMIN',
                        help='username for IPMI access')
    parser.add_argument('--password', default='ADMIN',
                        help='password for IPMI access')
    parser.add_argument('--jvm', default='/usr/lib/jvm/lw-oracle-jdk-8',
                        help='Directory of JVM')
    parser.add_argument('host', help='Host to access')
    args = parser.parse_args()
    launch_kvm(args)


if __name__ == '__main__':
    main()

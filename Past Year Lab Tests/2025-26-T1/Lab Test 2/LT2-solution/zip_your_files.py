import sys, os, zipfile
from datetime import datetime

config = {
    'LT_tag': 'LT2',                              # Tag prefixed to submission
    'LT_name': 'Lab Test 2',                      # Title rendered in terminal
    # Minimum set of files in complete submission        
    'file_names': ['q1a.py', 'q1b.py', 'q2a.py', 'q2b.py', 'q3a.py', 'q3b.py', 'q4a.py', 'q4b.py'],
    'test_start_date': '2025-11-17 09:00:00'           # Expect student solutions to have timestamp later
                                                       # than this time (local)
                                                       # %Y-%m-%d %H:%M:%S
}

class SubmissionClass:
    
    BLINK_ON   = '\033[5m'
    BLINK_OFF  = '\033[0m'
    BOLD_RED   = '\033[1;31m'
    BOLD_GREEN = '\033[1;32m'
    
    max_width = 50
    ##############################################################                
    def __init__(self, config):
        self.config = config
        title = f'{"*"*10}{self.config["LT_name"]} Submission Tool{"*"*10}'
        self.max_width = min(self.get_terminal_width(), len(title))
        print()
        print('*'*self.max_width)
        print(title)
        print('*'*self.max_width)
        
    ##############################################################                
    def get_terminal_width(self):
        try:
            return os.get_terminal_size().columns
        except OSError:
            return 30
        
    ##############################################################                
    def invalid_filename(self, fname):
        invalid_chars = '\n\t <>:"/\\|?*@'
        if not fname:
            return True
        for ch in fname:
            if ch in invalid_chars:
                return ch
        return False
    
    ##############################################################                        
    def is_modified(self, fname, config):
        timestamp = datetime.fromtimestamp(os.path.getmtime(fname))
        return timestamp > config['ref_date']
    
    ##############################################################                    
    def blink_str(self, st, color=None):
        if color is None:
            color = self.BOLD_RED
        return f'{color}{self.BLINK_ON}{st}{self.BLINK_OFF}'
    
    ##############################################################                
    def get_username(self):
        # Get username to name the archive
        while True:
            username = input('Enter your username: ')
            if not(self.invalid_filename(username)):
                return username
            if username == '':
                print('Username must not be empty.')                    
            elif '@' in username:
                print('Your username is the part of your email address to the left of "@".')
            else:
                print(f'Invalid character in username: "{self.invalid_filename(username)}"')
                
    ##############################################################                
    def make_zip(self, zfn, username, all_py_files):
        # Make the ZIP file
        with zipfile.ZipFile(zfn, mode='w') as zf:
            zf.writestr(username + '/', '')
            for f in all_py_files:
                zf.write(f, arcname=os.path.join(username,f))
            il = zf.infolist()

        # Print confirmation
        print()
        print('Archive Contents:')
        print(f'\t{"Size":10s}Filename')
        for i in il:
            print(f'\t{str(i.file_size):10s}{i.filename}')
        print()

    ##############################################################
    def get_files(self):
        # Get list of files
        my_name = os.path.basename(__file__)
        # Zip everything except prior zip files and subdirectories
        all_py_files = [f for f in os.listdir('.') if os.path.isfile(f) and
                        f != my_name and not f.endswith('.zip')]        
        all_py_files = sorted(all_py_files)

        # Check for missing files
        missing = []
        unmodified = []
        for fname in self.config['file_names']:
            if fname not in all_py_files:
                missing.append(fname)
            elif self.is_modified(fname, config) == False:
                unmodified.append(fname)
        return all_py_files, missing, unmodified

    ##############################################################
    def print_prefix(self, prefix, strings):
        for st in strings:
            print(prefix+st)

    ##############################################################                                
    def package(self, root_dir='.'):
        config['ref_date'] = datetime.strptime(config['test_start_date'], "%Y-%m-%d %H:%M:%S")
        os.chdir(root_dir)
        all_py_files, missing, unmodified = self.get_files()

        if not all_py_files:
            print(f'No Python files found in {root_dir}')            
            sys.exit(-1)
            
        if missing:
            print(f'The following files are {self.blink_str("MISSING:")}')
            self.print_prefix('\t', missing)
            print()
            
        if unmodified:
            print(f'The following files show {self.blink_str("NO CHANGES")} since', str(config['test_start_date'])+':')
            self.print_prefix('\t', unmodified)
            print()
            
        if missing or unmodified:
            while True: 
                ans = input('Is this correct? (y/n) ')
                if ans == 'y':
                    break
                if ans == 'n':
                    print('You have answered no.\nPlease correct the errors and try again.')
                    return

        print('The following files will be packaged for submission:')
        for f in all_py_files:
            print('\t',f)    
        print()
        
        while True:
            ans = input('Package the listed files? (y/n) ').lower()
            if ans == 'n':
                print('You have answered no.\nPlease try again.')                
                return
            if ans == 'y':
                break

        username = self.get_username()
        zfn = os.path.join(f'{self.config["LT_tag"]}-{username}.zip')
        self.make_zip(zfn, username, all_py_files)
        print(f'Submit this file via Examena: {self.blink_str(zfn, color=self.BOLD_GREEN)}')

def main():    
    pkg=SubmissionClass(config)
    dir_name = os.path.dirname(__file__)
    if not dir_name:
        dir_name = '.'
    print(f'Packaging files in {dir_name}')
    pkg.package(dir_name)
    
if __name__ == "__main__":
    main()

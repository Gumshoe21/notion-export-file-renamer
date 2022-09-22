import os
import re 

file_regexp = r'( \w{32,32}\b)'

def main():
	for root, dirs, files in os.walk(os.getcwd(), topdown=False):
			for f in files:
				f_path = os.path.join(root, f)
				subtitute_f_path = re.sub(file_regexp, '', os.path.abspath(f_path))
				os.renames(f_path, subtitute_f_path)

if __name__ == "__main__":
	main()
  
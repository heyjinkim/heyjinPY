from argparse import ArgumentParser

def get_params():
  parser = ArgumentParser(description="Heyjin's first argument control")
  parser.add_argument('name', help='The name passed to the function')
  return parser.parse_args()

def who_is_awesome(name):
  if name.upper() == 'HEYJIN':
    print "%s is AWESOME!" % name
  else:
    print "%s is NOT awesome." % name

def main():
  params = get_params()
  name = params.name
  who_is_awesome(name)

if __name__ == '__main__':
  main()
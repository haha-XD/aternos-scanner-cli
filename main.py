import argparse

import panos

def print_results(results):
    print('-----OUTPUT-----')
    for result in results:
        print(result)
    print('----------------')

def dump_results(results, outfile):
    with open(outfile, 'w+', encoding='utf-8') as f:
        print(f'Outputting results into {f.name}...')
        f.writelines([str(result) + '\n' for result in results])        
    print(f'Finished outputting results into {outfile}')

def get_args():
    parser = argparse.ArgumentParser(description='Scans given iprange for minecraft servers on port 25565.')
    parser.add_argument('option', nargs='*', 
                        help='mode used for scanning: [random, specific, full]')
    parser.add_argument('-f', '--filtering', default=None,
                        help='options for filtering.')
    parser.add_argument('-o', '--outfile', default=None,
                        help='options for filtering.')
    parser.add_argument('-v', '--verbose', type=bool, nargs='?', const=False, default=True)
    parser.add_argument('-s', '--silent', type=bool, nargs='?', const=True, default=False)
    args = parser.parse_args()
    return args

def main():
    args = get_args()

    option_dict = {'random' : panos.scan_random_aternos,
                   'specific' : panos.scan_specific_aternos,
                   'full' : panos.scan_full_aternos}
    if args.option[0] == 'specific' and len(args.option) == 2:
        results = option_dict[args.option[0]](args.option[1], filtering=args.filtering, silent=args.verbose)
    else:
        results = option_dict[args.option[0]](filtering=args.filtering, silent=args.verbose)
        
    if args.outfile:
        dump_results(results, args.outfile)
    if not args.silent:
        print_results(results)


if __name__ == '__main__':
    main()
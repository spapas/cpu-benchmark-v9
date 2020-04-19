import json

PREAMBLE = """
This is the performance test v 9 (PT9) of the well-known benchmarking page passmark.

I copied it from here: https://www.cpubenchmark.net/pt9_cpu_list.php for my own reference.

| CPU name  | CPU mark | Thread rating | Samples |
| --------- | -------- | ------------- | ------- |
"""

def main():
    with open('cpus.json') as fin:
        result = json.loads(fin.read())

    lines = []
    with open('README.md', "w") as fout:
        fout.write(PREAMBLE)

        for r in result:
            line = '|'
            line += r['name'] +'|'
            line += r['cpu_mark'] +'|'
            line += r['thread_rating'] +'|'
            line += r['samples'] +'|'
            # lines.append(line)
            fout.write(line)
            fout.write('\n')

if __name__ == '__main__':
    main()
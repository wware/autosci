import re

opener = re.compile(r"^\s*<<([-_*a-zA-Z][-_*a-zA-Z0-9 ]*)>>\s*=$")
link = re.compile(r"^\s*<<([-_*a-zA-Z][-_*a-zA-Z0-9 ]*)>>$")
closer = re.compile(r"^@$")


class Link(str):
    pass


class Parser(dict):
    def define_chunk(self, line, name):
        raise NotImplementedError

    def finish_chunk(self):
        raise NotImplementedError

    def line_in_chunk(self, line):
        raise NotImplementedError

    def line_outside_chunk(self, line):
        raise NotImplementedError

    def link_chunk(self, line, subname):
        raise NotImplementedError

    def read(self, infile):
        defining = None
        for line in infile.readlines():
            line = line.rstrip()
            if defining is None:
                assert link.match(line) is None, line
                assert closer.match(line) is None, line
                m = opener.match(line)
                if m is not None:
                    defining = m.group(1)
                    self.define_chunk(line, defining)
                else:
                    self.line_outside_chunk(line)
            else:
                assert opener.match(line) is None, line
                if closer.match(line):
                    self.finish_chunk()
                    defining = None
                else:
                    m = link.match(line)
                    if m is not None:
                        self.link_chunk(line, m.group(1))
                    else:
                        self.line_in_chunk(line)
        assert defining is None

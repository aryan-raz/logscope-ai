import re

class NginxParser:

    pattern = re.compile(
        r'(?P<ip>\S+)'
    )

    def parse(self, line):
        match = self.pattern.search(line)

        if not match:
            return None

        return match.groupdict()
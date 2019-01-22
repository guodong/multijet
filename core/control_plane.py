from core.space import Space
import json


class ControlPlane:
    def __init__(self, offset):
        self.offset = offset
        self.rules = []
        self.frules = {}  # forward rules, indexed by port
        self.pm = {}  # property matrix, property=>(port, Space)

    def add_rule(self, match, action):
        # check exists
        for rule in self.rules:
            if json.dumps(rule['match']) == json.dumps({"match": match}): # modify flow rule, TODO: cache json result or use more quicker check
                rule['action'] = action
                break

            if json.dumps(rule) == json.dumps({"match": match, "action": action}):  # TODO: use more quicker check
                return
        self.rules.append({"match": match, "action": action})
        self.calc_space()

    def get_output_space(self, output):
        space = Space()
        for rule in self.rules:
            if rule['output'] == output:
                space.plus(Space(rule['match']))

    # TODO: incremental calc
    def calc_space(self):
        for rule in self.rules:
            self.frules[rule['action']['output']] = Space(areas=[], match={})
        for rule in self.rules:
            self.frules[rule['action']['output']].plus(Space(areas=[], match=rule['match']))

        self.dump()

    def calc_property_space(self, in_port, property, areas):
        if not self.pm.has_key(property):
            # self.pm[property] = Space(areas=[], match={})
            self.pm[property] = {}

        if not self.pm[property].has_key(in_port):
            self.pm[property][in_port] = Space(areas=[], match={})

        space = Space(areas=[], match={})
        for forward_port in self.frules:
            if forward_port == in_port:
                space.plus(self.frules[forward_port])

        space.multiply(Space(areas=areas, match={}))

        self.dump()

        if self.equal(space, self.pm[property][in_port]):
            return False
        else:
            self.pm[property][in_port] = space
            return True

    # TODO: unordered areas compare
    def equal(self, space1, space2):
        space1.areas.sort()
        space2.areas.sort()
        if len(space1.areas) != len(space2.areas):
            return False

        for i in range(len(space2.areas)):
            if space1.areas[i] != space2.areas[i]:
                return False

        return True

    def get_property_areas(self, property):
        if not self.pm.has_key(property):
            return []

        result = []
        for space in self.pm[property].values():
            for a in space.areas:
                result.append(a)

        result.sort()
        return result

    def dump(self):
        with open('/tmp/cp' + str(self.offset), 'w') as f:
            f.write("rules:\n")
            for r in self.rules:
                f.write(json.dumps(r))
                f.write('\n')

            f.write('frules:\n')
            for fr, s in self.frules.items():
                f.write(str(fr))
                f.write(json.dumps(s.areas))
                f.write('\n')

            for p, s in self.pm.items():
                f.write(p + '\n')
                for port, space in s.items():
                    f.write(str(port))
                    for a in space.areas:
                        f.write(a)
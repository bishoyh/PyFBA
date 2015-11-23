import unittest

import PyFBA


class TestReactionRoles(unittest.TestCase):
    def test_reactions_to_roles(self):
        roles = PyFBA.filters.roles_and_reactions.reactions_to_roles({'rxn00001'})
        self.assertEqual(len(roles['rxn00001']), 4)
        self.assertIn('Inorganic pyrophosphatase (EC 3.6.1.1)', roles['rxn00001'])
        self.assertIn('Inorganic pyrophospatase PpaX', roles['rxn00001'])
        self.assertIn('Manganese-dependent inorganic pyrophosphatase (EC 3.6.1.1)', roles['rxn00001'])
        self.assertIn('Pyrophosphate-energized proton pump (EC 3.6.1.1)', roles['rxn00001'])

    def test_roles_to_reactions(self):
        hal = 'Histidine ammonia-lyase (EC 4.3.1.3)'
        glna = 'Glutamine synthetase (EC 6.3.1.2)'
        reactions = PyFBA.filters.roles_and_reactions.roles_to_reactions({hal, glna})
        # this should be a single member set and have one reaction rxn00867
        self.assertEqual(len(reactions[hal]), 1)
        self.assertIn('rxn00867', reactions[hal])
        self.assertEqual(len(reactions[glna]), 1)
        self.assertIn('rxn00187', reactions[glna])

if __name__ == '__main__':
    unittest.main()

import sys

__author__ = "Rob Edwards"


def suggest_from_media(compounds, reactions, reactions2run, media, verbose=False):
    """
    Suggest which reactions we should add to include media compounds

    :param reactions: Our reactions dict object
    :type reactions: dict
    :param verbose: Print more output
    :type verbose: bool
    :param compounds: Our compounds dictionary
    :type compounds: dict
    :param reactions2run: The reactions we are running
    :type reactions2run: set.
    :param media: A set of the compounds in the media
    :type media: set.
    :return: The suggested reactions
    :rtype: set.
    """

    # which compounds are in our media
    suggest = set()
    for c in media:
        rxns = compounds[str(c)].all_reactions()
        importrxn = rxns.intersection(reactions2run)
        if len(importrxn) == 0:
            if verbose:
                sys.stderr.write(str(c) + " is not imported\n")
            suggest.update(rxns)
    suggest = {r for r in suggest if r in reactions and r not in reactions2run}

    return suggest

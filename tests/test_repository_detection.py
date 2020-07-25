from repository_detection import all_platforms as platforms


def test_link_detection():
    from re import findall

    assert findall(platforms['zenodo'], 'https://doi.org/10.5281/zenodo.3548040') == ['zenodo.3548040']
    assert findall(platforms['zenodo'], '(https://doi.org/10.5281/zenodo.3548040).') == ['zenodo.3548040']

    assert findall(platforms['bioconductor'], 'http://bioconductor.org/packages/CancerSubtypes/') == ['CancerSubtypes/']

    assert findall(platforms['cran'], 'https://cran.r-project.org/package=LUCIDus') == ['LUCIDus']
    assert findall(platforms['cran'], 'https://cran.r-project.org/web/packages/Spectrum/index.html') == ['Spectrum/index.html']
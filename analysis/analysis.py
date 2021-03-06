import json
import os
import shutil
import scipy_data_fitting

import fits

def reset_directory(directory):
    """
    Remove `directory` if it exists, then create it if it doesn't exist.
    """
    if os.path.isdir(directory): shutil.rmtree(directory)
    if not os.path.isdir(directory): os.makedirs(directory)

def export_fit(fit, plot_directory=None, json_directory=None, meta=None):
    """
    Use `fit` to generate and save a plot to `plot_directory`
    and json to `json_directory`.

    If either `plot_directory` or `json_directory` are not given,
    the corresponding plot or json will not be saved.

    If `meta` is given, it will be included in the fit's json file.
    """
    name = fit.name

    if json_directory:
        fit.to_json(os.path.join(json_directory, name + '.json'), points=500, meta=meta)

    if plot_directory:
        plot = scipy_data_fitting.Plot(fit)
        plot.save(os.path.join(plot_directory, name + '.svg'), transparent=True)
        plot.close()

def figure_4():
    """
    Returns a list of subfigure tuples that will be
    passed to `fits.NonZeroFieldParallel`, etc.

    Tuple format is `(subfig_letter, contact_spacing_(L))`,
    e.g. `('a', 2.1)`.

    See `analysis.all_fits`.
    """
    return [
        ('a', 2.1),
        ('b', 5.5),
        ('c', 2.0),
        ('d', 3.0),
    ]

def all_fits():
    """
    Returns a list of all well defined fits that can be plotted, etc.

    Fits are of the type `scipy_data_fitting.Fit`.
    """
    all_fits = []
    for fig in figure_4():
        all_fits.append(fits.NonZeroFieldParallel(fig))
        all_fits.append(fits.NonZeroFieldAntiparallel(fig))
        all_fits.append(fits.NonZeroFieldNormalizedParallel(fig))
        all_fits.append(fits.NonZeroFieldNormalizedAntiparallel(fig))
        all_fits.append(fits.TransparentContactsParallel(fig))
        all_fits.append(fits.TransparentContactsAntiparallel(fig))
        # all_fits.append(fits.TransparentContactsNormalizedParallel(fig))
        # all_fits.append(fits.TransparentContactsNormalizedAntiparallel(fig))

        if not fig[0] == 'c':
            all_fits.append(fits.NonZeroFieldDifference(fig))
            all_fits.append(fits.NonZeroFieldNormalizedDifference(fig))
            all_fits.append(fits.TransparentContactsDifference(fig))
            # all_fits.append(fits.TransparentContactsNormalizedDifference(fig))

    return all_fits

def save_fits(fits,
        plot_directory=os.path.join('build', 'plots'),
        json_directory=os.path.join('build', 'json'),
        with_meta=False, with_meta_file=True):
    """
    Each fit in `fits` will generate a plot in `plot_directory`
    and a json file in `json_directory`.

    Additionally, `fits.json` will be created in `json_directory` with metadata for each fit.

    If either `plot_directory` or `json_directory` are not given,
    the corresponding plots or json will not be saved.

    If `with_meta` is `True`, then metadata will also be saved in the json file for each fit.

    See also `analysis.export_fit`.
    """
    if json_directory: reset_directory(json_directory)
    if plot_directory: reset_directory(plot_directory)

    fit_metadata = []
    for fit in fits:
        meta = fit.metadata
        meta['quality'] = []

        if hasattr(fit.curve_fit, 'chisqr'):
            meta['quality'].append({ 'name': 'Chi-squared', 'value': fit.curve_fit.chisqr})

        included_meta = None
        if with_meta: included_meta = meta

        export_fit(fit, plot_directory, json_directory, meta=included_meta)

        fit_metadata.append(meta)

    if json_directory and with_meta_file:
        f = open(os.path.join(json_directory, 'fits.json'), 'w')
        json.dump(fit_metadata, f)
        f.close

def main():
    """
    This is called when the analysis module (this module) is called from the interpreter.
    """
    fits = all_fits()
    save_fits(fits, with_meta=True, with_meta_file=False)
    save_fits(fits,
        plot_directory=False,
        json_directory=os.path.join('build', 'fitalyzer'))


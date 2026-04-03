---
layout: container
name:  "quay.io/biocontainers/ntsynt-viz"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ntsynt-viz/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ntsynt-viz/container.yaml"
updated_at: "2026-04-03 05:10:45.865235"
latest: "1.0.2--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/ntsynt-viz"
aliases:
 - "convert_distance_matrix_to_phylip.py"
 - "ntsynt_viz.py"
 - "ntsynt_viz.smk"
 - "ntsynt_viz_distance_cladogram.R"
 - "ntsynt_viz_find_plot_nudges.py"
 - "ntsynt_viz_format_blocks_gggenomes.py"
 - "ntsynt_viz_normalize_strands.py"
 - "ntsynt_viz_output_orders.py"
 - "ntsynt_viz_plot_synteny_blocks_ribbon_plot.R"
 - "ntsynt_viz_sort_sequences.py"
 - "ntsynt_viz_synteny_distance_estimation.py"
 - "quicktree"
 - "rename_synteny_blocks.py"
 - "sort_ntsynt_blocks.py"
 - "phc"
 - "eido"
 - "typer"
 - "rst2html"
 - "rst2html4"
 - "rst2html5"
 - "rst2latex"
 - "rst2man"
 - "rst2odt"
 - "rst2pseudoxml"
 - "rst2s5"
 - "rst2xetex"
 - "rst2xml"
 - "pandoc-lua"
 - "pandoc-server"
 - "yte"
 - "coloredlogs"
 - "docutils"
 - "pulptest"
 - "snakemake"
 - "cbc"
 - "clp"
 - "markdown-it"
 - "humanfriendly"
 - "jupyter-trust"
versions:
 - "1.0.1--hdfd78af_0"
 - "1.0.2--hdfd78af_1"
description: "singularity registry hpc automated addition for ntsynt-viz"
config: {"url": "https://biocontainers.pro/tools/ntsynt-viz", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for ntsynt-viz", "latest": {"1.0.2--hdfd78af_1": "sha256:0da3f3a1f7986fb9a8a2d0951823e20c3dc9477112926fb0e4c87720e90c990d"}, "tags": {"1.0.1--hdfd78af_0": "sha256:3da6486c8edeb1717f274068f9445d614319f820de49228e09dd2bdd3f879a2d", "1.0.2--hdfd78af_1": "sha256:0da3f3a1f7986fb9a8a2d0951823e20c3dc9477112926fb0e4c87720e90c990d"}, "docker": "quay.io/biocontainers/ntsynt-viz", "aliases": {"convert_distance_matrix_to_phylip.py": "/usr/local/bin/convert_distance_matrix_to_phylip.py", "ntsynt_viz.py": "/usr/local/bin/ntsynt_viz.py", "ntsynt_viz.smk": "/usr/local/bin/ntsynt_viz.smk", "ntsynt_viz_distance_cladogram.R": "/usr/local/bin/ntsynt_viz_distance_cladogram.R", "ntsynt_viz_find_plot_nudges.py": "/usr/local/bin/ntsynt_viz_find_plot_nudges.py", "ntsynt_viz_format_blocks_gggenomes.py": "/usr/local/bin/ntsynt_viz_format_blocks_gggenomes.py", "ntsynt_viz_normalize_strands.py": "/usr/local/bin/ntsynt_viz_normalize_strands.py", "ntsynt_viz_output_orders.py": "/usr/local/bin/ntsynt_viz_output_orders.py", "ntsynt_viz_plot_synteny_blocks_ribbon_plot.R": "/usr/local/bin/ntsynt_viz_plot_synteny_blocks_ribbon_plot.R", "ntsynt_viz_sort_sequences.py": "/usr/local/bin/ntsynt_viz_sort_sequences.py", "ntsynt_viz_synteny_distance_estimation.py": "/usr/local/bin/ntsynt_viz_synteny_distance_estimation.py", "quicktree": "/usr/local/bin/quicktree", "rename_synteny_blocks.py": "/usr/local/bin/rename_synteny_blocks.py", "sort_ntsynt_blocks.py": "/usr/local/bin/sort_ntsynt_blocks.py", "phc": "/usr/local/bin/phc", "eido": "/usr/local/bin/eido", "typer": "/usr/local/bin/typer", "rst2html": "/usr/local/bin/rst2html", "rst2html4": "/usr/local/bin/rst2html4", "rst2html5": "/usr/local/bin/rst2html5", "rst2latex": "/usr/local/bin/rst2latex", "rst2man": "/usr/local/bin/rst2man", "rst2odt": "/usr/local/bin/rst2odt", "rst2pseudoxml": "/usr/local/bin/rst2pseudoxml", "rst2s5": "/usr/local/bin/rst2s5", "rst2xetex": "/usr/local/bin/rst2xetex", "rst2xml": "/usr/local/bin/rst2xml", "pandoc-lua": "/usr/local/bin/pandoc-lua", "pandoc-server": "/usr/local/bin/pandoc-server", "yte": "/usr/local/bin/yte", "coloredlogs": "/usr/local/bin/coloredlogs", "docutils": "/usr/local/bin/docutils", "pulptest": "/usr/local/bin/pulptest", "snakemake": "/usr/local/bin/snakemake", "cbc": "/usr/local/bin/cbc", "clp": "/usr/local/bin/clp", "markdown-it": "/usr/local/bin/markdown-it", "humanfriendly": "/usr/local/bin/humanfriendly", "jupyter-trust": "/usr/local/bin/jupyter-trust"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ntsynt-viz.
singularity registry hpc automated addition for ntsynt-viz
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ntsynt-viz
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ntsynt-viz:1.0.2--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ntsynt-viz/1.0.2--hdfd78af_1
$ module help quay.io/biocontainers/ntsynt-viz/1.0.2--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ntsynt-viz-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ntsynt-viz-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ntsynt-viz-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ntsynt-viz-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ntsynt-viz-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ntsynt-viz-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### convert_distance_matrix_to_phylip.py

```bash
$ singularity exec <container> /usr/local/bin/convert_distance_matrix_to_phylip.py
$ podman run --it --rm --entrypoint /usr/local/bin/convert_distance_matrix_to_phylip.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert_distance_matrix_to_phylip.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ntsynt_viz.py

```bash
$ singularity exec <container> /usr/local/bin/ntsynt_viz.py
$ podman run --it --rm --entrypoint /usr/local/bin/ntsynt_viz.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ntsynt_viz.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ntsynt_viz.smk

```bash
$ singularity exec <container> /usr/local/bin/ntsynt_viz.smk
$ podman run --it --rm --entrypoint /usr/local/bin/ntsynt_viz.smk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ntsynt_viz.smk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ntsynt_viz_distance_cladogram.R

```bash
$ singularity exec <container> /usr/local/bin/ntsynt_viz_distance_cladogram.R
$ podman run --it --rm --entrypoint /usr/local/bin/ntsynt_viz_distance_cladogram.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ntsynt_viz_distance_cladogram.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ntsynt_viz_find_plot_nudges.py

```bash
$ singularity exec <container> /usr/local/bin/ntsynt_viz_find_plot_nudges.py
$ podman run --it --rm --entrypoint /usr/local/bin/ntsynt_viz_find_plot_nudges.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ntsynt_viz_find_plot_nudges.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ntsynt_viz_format_blocks_gggenomes.py

```bash
$ singularity exec <container> /usr/local/bin/ntsynt_viz_format_blocks_gggenomes.py
$ podman run --it --rm --entrypoint /usr/local/bin/ntsynt_viz_format_blocks_gggenomes.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ntsynt_viz_format_blocks_gggenomes.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ntsynt_viz_normalize_strands.py

```bash
$ singularity exec <container> /usr/local/bin/ntsynt_viz_normalize_strands.py
$ podman run --it --rm --entrypoint /usr/local/bin/ntsynt_viz_normalize_strands.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ntsynt_viz_normalize_strands.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ntsynt_viz_output_orders.py

```bash
$ singularity exec <container> /usr/local/bin/ntsynt_viz_output_orders.py
$ podman run --it --rm --entrypoint /usr/local/bin/ntsynt_viz_output_orders.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ntsynt_viz_output_orders.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ntsynt_viz_plot_synteny_blocks_ribbon_plot.R

```bash
$ singularity exec <container> /usr/local/bin/ntsynt_viz_plot_synteny_blocks_ribbon_plot.R
$ podman run --it --rm --entrypoint /usr/local/bin/ntsynt_viz_plot_synteny_blocks_ribbon_plot.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ntsynt_viz_plot_synteny_blocks_ribbon_plot.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ntsynt_viz_sort_sequences.py

```bash
$ singularity exec <container> /usr/local/bin/ntsynt_viz_sort_sequences.py
$ podman run --it --rm --entrypoint /usr/local/bin/ntsynt_viz_sort_sequences.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ntsynt_viz_sort_sequences.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ntsynt_viz_synteny_distance_estimation.py

```bash
$ singularity exec <container> /usr/local/bin/ntsynt_viz_synteny_distance_estimation.py
$ podman run --it --rm --entrypoint /usr/local/bin/ntsynt_viz_synteny_distance_estimation.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ntsynt_viz_synteny_distance_estimation.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quicktree

```bash
$ singularity exec <container> /usr/local/bin/quicktree
$ podman run --it --rm --entrypoint /usr/local/bin/quicktree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quicktree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rename_synteny_blocks.py

```bash
$ singularity exec <container> /usr/local/bin/rename_synteny_blocks.py
$ podman run --it --rm --entrypoint /usr/local/bin/rename_synteny_blocks.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rename_synteny_blocks.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sort_ntsynt_blocks.py

```bash
$ singularity exec <container> /usr/local/bin/sort_ntsynt_blocks.py
$ podman run --it --rm --entrypoint /usr/local/bin/sort_ntsynt_blocks.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sort_ntsynt_blocks.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phc

```bash
$ singularity exec <container> /usr/local/bin/phc
$ podman run --it --rm --entrypoint /usr/local/bin/phc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eido

```bash
$ singularity exec <container> /usr/local/bin/eido
$ podman run --it --rm --entrypoint /usr/local/bin/eido   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eido   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### typer

```bash
$ singularity exec <container> /usr/local/bin/typer
$ podman run --it --rm --entrypoint /usr/local/bin/typer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/typer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2html

```bash
$ singularity exec <container> /usr/local/bin/rst2html
$ podman run --it --rm --entrypoint /usr/local/bin/rst2html   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2html   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2html4

```bash
$ singularity exec <container> /usr/local/bin/rst2html4
$ podman run --it --rm --entrypoint /usr/local/bin/rst2html4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2html4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2html5

```bash
$ singularity exec <container> /usr/local/bin/rst2html5
$ podman run --it --rm --entrypoint /usr/local/bin/rst2html5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2html5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2latex

```bash
$ singularity exec <container> /usr/local/bin/rst2latex
$ podman run --it --rm --entrypoint /usr/local/bin/rst2latex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2latex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2man

```bash
$ singularity exec <container> /usr/local/bin/rst2man
$ podman run --it --rm --entrypoint /usr/local/bin/rst2man   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2man   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2odt

```bash
$ singularity exec <container> /usr/local/bin/rst2odt
$ podman run --it --rm --entrypoint /usr/local/bin/rst2odt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2odt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2pseudoxml

```bash
$ singularity exec <container> /usr/local/bin/rst2pseudoxml
$ podman run --it --rm --entrypoint /usr/local/bin/rst2pseudoxml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2pseudoxml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2s5

```bash
$ singularity exec <container> /usr/local/bin/rst2s5
$ podman run --it --rm --entrypoint /usr/local/bin/rst2s5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2s5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2xetex

```bash
$ singularity exec <container> /usr/local/bin/rst2xetex
$ podman run --it --rm --entrypoint /usr/local/bin/rst2xetex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2xetex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2xml

```bash
$ singularity exec <container> /usr/local/bin/rst2xml
$ podman run --it --rm --entrypoint /usr/local/bin/rst2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc-lua

```bash
$ singularity exec <container> /usr/local/bin/pandoc-lua
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc-lua   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc-lua   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc-server

```bash
$ singularity exec <container> /usr/local/bin/pandoc-server
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### yte

```bash
$ singularity exec <container> /usr/local/bin/yte
$ podman run --it --rm --entrypoint /usr/local/bin/yte   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yte   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coloredlogs

```bash
$ singularity exec <container> /usr/local/bin/coloredlogs
$ podman run --it --rm --entrypoint /usr/local/bin/coloredlogs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coloredlogs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### docutils

```bash
$ singularity exec <container> /usr/local/bin/docutils
$ podman run --it --rm --entrypoint /usr/local/bin/docutils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/docutils   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pulptest

```bash
$ singularity exec <container> /usr/local/bin/pulptest
$ podman run --it --rm --entrypoint /usr/local/bin/pulptest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pulptest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snakemake

```bash
$ singularity exec <container> /usr/local/bin/snakemake
$ podman run --it --rm --entrypoint /usr/local/bin/snakemake   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snakemake   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cbc

```bash
$ singularity exec <container> /usr/local/bin/cbc
$ podman run --it --rm --entrypoint /usr/local/bin/cbc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cbc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clp

```bash
$ singularity exec <container> /usr/local/bin/clp
$ podman run --it --rm --entrypoint /usr/local/bin/clp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### markdown-it

```bash
$ singularity exec <container> /usr/local/bin/markdown-it
$ podman run --it --rm --entrypoint /usr/local/bin/markdown-it   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/markdown-it   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### humanfriendly

```bash
$ singularity exec <container> /usr/local/bin/humanfriendly
$ podman run --it --rm --entrypoint /usr/local/bin/humanfriendly   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/humanfriendly   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-trust

```bash
$ singularity exec <container> /usr/local/bin/jupyter-trust
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-trust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-trust   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>

### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)
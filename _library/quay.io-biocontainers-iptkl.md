---
layout: container
name:  "quay.io/biocontainers/iptkl"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/iptkl/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/iptkl/container.yaml"
updated_at: "2022-10-27 00:38:17.457186"
latest: "0.6.8--pyh5e36f6f_0"
container_url: "https://biocontainers.pro/tools/iptkl"
aliases:
 - "colorcet"
 - "compare_gos.py"
 - "go_plot.py"
 - "holoviews"
 - "ncbi_gene_results_to_python.py"
 - "nglview"
 - "panel"
 - "prt_terms.py"
 - "wr_hier.py"
 - "wr_sections.py"
versions:
 - "0.6.8--pyh5e36f6f_0"
description: "shpc-registry automated BioContainers addition for iptkl"
config: {"url": "https://biocontainers.pro/tools/iptkl", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for iptkl", "latest": {"0.6.8--pyh5e36f6f_0": "sha256:424140b2aadbd8b303569b7fb1f08117fea473944acddb10b78725724e7645c3"}, "tags": {"0.6.8--pyh5e36f6f_0": "sha256:424140b2aadbd8b303569b7fb1f08117fea473944acddb10b78725724e7645c3"}, "docker": "quay.io/biocontainers/iptkl", "aliases": {"colorcet": "/usr/local/bin/colorcet", "compare_gos.py": "/usr/local/bin/compare_gos.py", "go_plot.py": "/usr/local/bin/go_plot.py", "holoviews": "/usr/local/bin/holoviews", "ncbi_gene_results_to_python.py": "/usr/local/bin/ncbi_gene_results_to_python.py", "nglview": "/usr/local/bin/nglview", "panel": "/usr/local/bin/panel", "prt_terms.py": "/usr/local/bin/prt_terms.py", "wr_hier.py": "/usr/local/bin/wr_hier.py", "wr_sections.py": "/usr/local/bin/wr_sections.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/iptkl.
shpc-registry automated BioContainers addition for iptkl
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/iptkl
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/iptkl:0.6.8--pyh5e36f6f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/iptkl/0.6.8--pyh5e36f6f_0
$ module help quay.io/biocontainers/iptkl/0.6.8--pyh5e36f6f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### iptkl-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### iptkl-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### iptkl-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### iptkl-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### iptkl-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### iptkl-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### colorcet

```bash
$ singularity exec <container> /usr/local/bin/colorcet
$ podman run --it --rm --entrypoint /usr/local/bin/colorcet   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/colorcet   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compare_gos.py

```bash
$ singularity exec <container> /usr/local/bin/compare_gos.py
$ podman run --it --rm --entrypoint /usr/local/bin/compare_gos.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compare_gos.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### go_plot.py

```bash
$ singularity exec <container> /usr/local/bin/go_plot.py
$ podman run --it --rm --entrypoint /usr/local/bin/go_plot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/go_plot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### holoviews

```bash
$ singularity exec <container> /usr/local/bin/holoviews
$ podman run --it --rm --entrypoint /usr/local/bin/holoviews   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/holoviews   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncbi_gene_results_to_python.py

```bash
$ singularity exec <container> /usr/local/bin/ncbi_gene_results_to_python.py
$ podman run --it --rm --entrypoint /usr/local/bin/ncbi_gene_results_to_python.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncbi_gene_results_to_python.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nglview

```bash
$ singularity exec <container> /usr/local/bin/nglview
$ podman run --it --rm --entrypoint /usr/local/bin/nglview   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nglview   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### panel

```bash
$ singularity exec <container> /usr/local/bin/panel
$ podman run --it --rm --entrypoint /usr/local/bin/panel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/panel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prt_terms.py

```bash
$ singularity exec <container> /usr/local/bin/prt_terms.py
$ podman run --it --rm --entrypoint /usr/local/bin/prt_terms.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prt_terms.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wr_hier.py

```bash
$ singularity exec <container> /usr/local/bin/wr_hier.py
$ podman run --it --rm --entrypoint /usr/local/bin/wr_hier.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wr_hier.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wr_sections.py

```bash
$ singularity exec <container> /usr/local/bin/wr_sections.py
$ podman run --it --rm --entrypoint /usr/local/bin/wr_sections.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wr_sections.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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
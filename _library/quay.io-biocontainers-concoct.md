---
layout: container
name:  "quay.io/biocontainers/concoct"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/concoct/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/concoct/container.yaml"
updated_at: "2022-10-27 00:57:32.424153"
latest: "1.1.0--py310h74abf4b_3"
container_url: "https://biocontainers.pro/tools/concoct"
aliases:
 - "concoct"
 - "concoct_coverage_table.py"
 - "concoct_refine"
 - "cut_up_fasta.py"
 - "extract_fasta_bins.py"
 - "merge_cutup_clustering.py"
versions:
 - "1.1.0--py310h74abf4b_3"
description: "shpc-registry automated BioContainers addition for concoct"
config: {"url": "https://biocontainers.pro/tools/concoct", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for concoct", "latest": {"1.1.0--py310h74abf4b_3": "sha256:109756b95a510daac9a52b9bb54520c065694eccbaff5a1ff8a502747ec297f5"}, "tags": {"1.1.0--py310h74abf4b_3": "sha256:109756b95a510daac9a52b9bb54520c065694eccbaff5a1ff8a502747ec297f5"}, "docker": "quay.io/biocontainers/concoct", "aliases": {"concoct": "/usr/local/bin/concoct", "concoct_coverage_table.py": "/usr/local/bin/concoct_coverage_table.py", "concoct_refine": "/usr/local/bin/concoct_refine", "cut_up_fasta.py": "/usr/local/bin/cut_up_fasta.py", "extract_fasta_bins.py": "/usr/local/bin/extract_fasta_bins.py", "merge_cutup_clustering.py": "/usr/local/bin/merge_cutup_clustering.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/concoct.
shpc-registry automated BioContainers addition for concoct
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/concoct
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/concoct:1.1.0--py310h74abf4b_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/concoct/1.1.0--py310h74abf4b_3
$ module help quay.io/biocontainers/concoct/1.1.0--py310h74abf4b_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### concoct-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### concoct-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### concoct-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### concoct-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### concoct-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### concoct-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### concoct

```bash
$ singularity exec <container> /usr/local/bin/concoct
$ podman run --it --rm --entrypoint /usr/local/bin/concoct   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/concoct   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### concoct_coverage_table.py

```bash
$ singularity exec <container> /usr/local/bin/concoct_coverage_table.py
$ podman run --it --rm --entrypoint /usr/local/bin/concoct_coverage_table.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/concoct_coverage_table.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### concoct_refine

```bash
$ singularity exec <container> /usr/local/bin/concoct_refine
$ podman run --it --rm --entrypoint /usr/local/bin/concoct_refine   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/concoct_refine   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cut_up_fasta.py

```bash
$ singularity exec <container> /usr/local/bin/cut_up_fasta.py
$ podman run --it --rm --entrypoint /usr/local/bin/cut_up_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cut_up_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_fasta_bins.py

```bash
$ singularity exec <container> /usr/local/bin/extract_fasta_bins.py
$ podman run --it --rm --entrypoint /usr/local/bin/extract_fasta_bins.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_fasta_bins.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge_cutup_clustering.py

```bash
$ singularity exec <container> /usr/local/bin/merge_cutup_clustering.py
$ podman run --it --rm --entrypoint /usr/local/bin/merge_cutup_clustering.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge_cutup_clustering.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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
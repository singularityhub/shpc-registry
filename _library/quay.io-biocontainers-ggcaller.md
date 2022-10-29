---
layout: container
name:  "quay.io/biocontainers/ggcaller"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ggcaller/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/ggcaller/container.yaml"
updated_at: "2022-10-29 05:46:23.364087"
latest: "1.3.0--py38hee2cf1e_1"
container_url: "https://biocontainers.pro/tools/ggcaller"
aliases:
 - "Bifrost"
 - "ggcaller"
 - "rapidnj"
 - "2to3-3.8"
 - "FET.pl"
 - "activate-global-python-argcomplete"
 - "aggregate_scores_in_intervals.py"
 - "align_print_template.py"
 - "alimask"
 - "axt_extract_ranges.py"
 - "axt_to_fasta.py"
 - "axt_to_lav.py"
 - "axt_to_maf.py"
versions:
 - "1.3.0--py38hee2cf1e_1"
description: "shpc-registry automated BioContainers addition for ggcaller"
config: {"url": "https://biocontainers.pro/tools/ggcaller", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ggcaller", "latest": {"1.3.0--py38hee2cf1e_1": "sha256:83f27a9a7b57fa0c0fe140774c18b4992d8678fff7291edd3a7718b931f3b412"}, "tags": {"1.3.0--py38hee2cf1e_1": "sha256:83f27a9a7b57fa0c0fe140774c18b4992d8678fff7291edd3a7718b931f3b412"}, "docker": "quay.io/biocontainers/ggcaller", "aliases": {"Bifrost": "/usr/local/bin/Bifrost", "ggcaller": "/usr/local/bin/ggcaller", "rapidnj": "/usr/local/bin/rapidnj", "2to3-3.8": "/usr/local/bin/2to3-3.8", "FET.pl": "/usr/local/bin/FET.pl", "activate-global-python-argcomplete": "/usr/local/bin/activate-global-python-argcomplete", "aggregate_scores_in_intervals.py": "/usr/local/bin/aggregate_scores_in_intervals.py", "align_print_template.py": "/usr/local/bin/align_print_template.py", "alimask": "/usr/local/bin/alimask", "axt_extract_ranges.py": "/usr/local/bin/axt_extract_ranges.py", "axt_to_fasta.py": "/usr/local/bin/axt_to_fasta.py", "axt_to_lav.py": "/usr/local/bin/axt_to_lav.py", "axt_to_maf.py": "/usr/local/bin/axt_to_maf.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ggcaller.
shpc-registry automated BioContainers addition for ggcaller
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ggcaller
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ggcaller:1.3.0--py38hee2cf1e_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ggcaller/1.3.0--py38hee2cf1e_1
$ module help quay.io/biocontainers/ggcaller/1.3.0--py38hee2cf1e_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ggcaller-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ggcaller-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ggcaller-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ggcaller-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ggcaller-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ggcaller-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Bifrost

```bash
$ singularity exec <container> /usr/local/bin/Bifrost
$ podman run --it --rm --entrypoint /usr/local/bin/Bifrost   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Bifrost   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ggcaller

```bash
$ singularity exec <container> /usr/local/bin/ggcaller
$ podman run --it --rm --entrypoint /usr/local/bin/ggcaller   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ggcaller   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rapidnj

```bash
$ singularity exec <container> /usr/local/bin/rapidnj
$ podman run --it --rm --entrypoint /usr/local/bin/rapidnj   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rapidnj   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.8

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.8
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FET.pl

```bash
$ singularity exec <container> /usr/local/bin/FET.pl
$ podman run --it --rm --entrypoint /usr/local/bin/FET.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FET.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### activate-global-python-argcomplete

```bash
$ singularity exec <container> /usr/local/bin/activate-global-python-argcomplete
$ podman run --it --rm --entrypoint /usr/local/bin/activate-global-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/activate-global-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aggregate_scores_in_intervals.py

```bash
$ singularity exec <container> /usr/local/bin/aggregate_scores_in_intervals.py
$ podman run --it --rm --entrypoint /usr/local/bin/aggregate_scores_in_intervals.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aggregate_scores_in_intervals.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### align_print_template.py

```bash
$ singularity exec <container> /usr/local/bin/align_print_template.py
$ podman run --it --rm --entrypoint /usr/local/bin/align_print_template.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/align_print_template.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alimask

```bash
$ singularity exec <container> /usr/local/bin/alimask
$ podman run --it --rm --entrypoint /usr/local/bin/alimask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alimask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### axt_extract_ranges.py

```bash
$ singularity exec <container> /usr/local/bin/axt_extract_ranges.py
$ podman run --it --rm --entrypoint /usr/local/bin/axt_extract_ranges.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/axt_extract_ranges.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### axt_to_fasta.py

```bash
$ singularity exec <container> /usr/local/bin/axt_to_fasta.py
$ podman run --it --rm --entrypoint /usr/local/bin/axt_to_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/axt_to_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### axt_to_lav.py

```bash
$ singularity exec <container> /usr/local/bin/axt_to_lav.py
$ podman run --it --rm --entrypoint /usr/local/bin/axt_to_lav.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/axt_to_lav.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### axt_to_maf.py

```bash
$ singularity exec <container> /usr/local/bin/axt_to_maf.py
$ podman run --it --rm --entrypoint /usr/local/bin/axt_to_maf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/axt_to_maf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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
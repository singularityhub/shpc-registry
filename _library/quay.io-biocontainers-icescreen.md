---
layout: container
name:  "quay.io/biocontainers/icescreen"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/icescreen/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/icescreen/container.yaml"
updated_at: "2022-10-29 05:43:34.542031"
latest: "1.0.4--py310hdfd78af_1"
container_url: "https://biocontainers.pro/tools/icescreen"
aliases:
 - "AUTHORS.txt"
 - "INSTALL"
 - "LICENCE.txt"
 - "LOG_public_releases"
 - "agpl-3.0.txt"
 - "icescreen"
 - "2to3-3.10"
 - "accn-at-a-time"
 - "aggregate_scores_in_intervals.py"
 - "align-columns"
 - "align_print_template.py"
 - "alimask"
 - "amino-acid-composition"
 - "archive-pubmed"
 - "asn2xml"
 - "axt_extract_ranges.py"
versions:
 - "1.0.4--py310hdfd78af_1"
description: "shpc-registry automated BioContainers addition for icescreen"
config: {"url": "https://biocontainers.pro/tools/icescreen", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for icescreen", "latest": {"1.0.4--py310hdfd78af_1": "sha256:f47e05529012f861315b89a6ef1fa960f4ab16a92ee65c5e750f855f3025c1cd"}, "tags": {"1.0.4--py310hdfd78af_1": "sha256:f47e05529012f861315b89a6ef1fa960f4ab16a92ee65c5e750f855f3025c1cd"}, "docker": "quay.io/biocontainers/icescreen", "aliases": {"AUTHORS.txt": "/usr/local/bin/AUTHORS.txt", "INSTALL": "/usr/local/bin/INSTALL", "LICENCE.txt": "/usr/local/bin/LICENCE.txt", "LOG_public_releases": "/usr/local/bin/LOG_public_releases", "agpl-3.0.txt": "/usr/local/bin/agpl-3.0.txt", "icescreen": "/usr/local/bin/icescreen", "2to3-3.10": "/usr/local/bin/2to3-3.10", "accn-at-a-time": "/usr/local/bin/accn-at-a-time", "aggregate_scores_in_intervals.py": "/usr/local/bin/aggregate_scores_in_intervals.py", "align-columns": "/usr/local/bin/align-columns", "align_print_template.py": "/usr/local/bin/align_print_template.py", "alimask": "/usr/local/bin/alimask", "amino-acid-composition": "/usr/local/bin/amino-acid-composition", "archive-pubmed": "/usr/local/bin/archive-pubmed", "asn2xml": "/usr/local/bin/asn2xml", "axt_extract_ranges.py": "/usr/local/bin/axt_extract_ranges.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/icescreen.
shpc-registry automated BioContainers addition for icescreen
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/icescreen
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/icescreen:1.0.4--py310hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/icescreen/1.0.4--py310hdfd78af_1
$ module help quay.io/biocontainers/icescreen/1.0.4--py310hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### icescreen-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### icescreen-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### icescreen-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### icescreen-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### icescreen-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### icescreen-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### AUTHORS.txt

```bash
$ singularity exec <container> /usr/local/bin/AUTHORS.txt
$ podman run --it --rm --entrypoint /usr/local/bin/AUTHORS.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AUTHORS.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### INSTALL

```bash
$ singularity exec <container> /usr/local/bin/INSTALL
$ podman run --it --rm --entrypoint /usr/local/bin/INSTALL   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/INSTALL   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### LICENCE.txt

```bash
$ singularity exec <container> /usr/local/bin/LICENCE.txt
$ podman run --it --rm --entrypoint /usr/local/bin/LICENCE.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LICENCE.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### LOG_public_releases

```bash
$ singularity exec <container> /usr/local/bin/LOG_public_releases
$ podman run --it --rm --entrypoint /usr/local/bin/LOG_public_releases   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LOG_public_releases   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### agpl-3.0.txt

```bash
$ singularity exec <container> /usr/local/bin/agpl-3.0.txt
$ podman run --it --rm --entrypoint /usr/local/bin/agpl-3.0.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/agpl-3.0.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### icescreen

```bash
$ singularity exec <container> /usr/local/bin/icescreen
$ podman run --it --rm --entrypoint /usr/local/bin/icescreen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/icescreen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### accn-at-a-time

```bash
$ singularity exec <container> /usr/local/bin/accn-at-a-time
$ podman run --it --rm --entrypoint /usr/local/bin/accn-at-a-time   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/accn-at-a-time   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aggregate_scores_in_intervals.py

```bash
$ singularity exec <container> /usr/local/bin/aggregate_scores_in_intervals.py
$ podman run --it --rm --entrypoint /usr/local/bin/aggregate_scores_in_intervals.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aggregate_scores_in_intervals.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### align-columns

```bash
$ singularity exec <container> /usr/local/bin/align-columns
$ podman run --it --rm --entrypoint /usr/local/bin/align-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/align-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### amino-acid-composition

```bash
$ singularity exec <container> /usr/local/bin/amino-acid-composition
$ podman run --it --rm --entrypoint /usr/local/bin/amino-acid-composition   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amino-acid-composition   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archive-pubmed

```bash
$ singularity exec <container> /usr/local/bin/archive-pubmed
$ podman run --it --rm --entrypoint /usr/local/bin/archive-pubmed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archive-pubmed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asn2xml

```bash
$ singularity exec <container> /usr/local/bin/asn2xml
$ podman run --it --rm --entrypoint /usr/local/bin/asn2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asn2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### axt_extract_ranges.py

```bash
$ singularity exec <container> /usr/local/bin/axt_extract_ranges.py
$ podman run --it --rm --entrypoint /usr/local/bin/axt_extract_ranges.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/axt_extract_ranges.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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
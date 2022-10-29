---
layout: container
name:  "quay.io/biocontainers/gemini"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gemini/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/gemini/container.yaml"
updated_at: "2022-10-29 05:55:24.434739"
latest: "0.30.2--py27h6a6cfb3_5"
container_url: "https://biocontainers.pro/tools/gemini"
aliases:
 - "bottle.py"
 - "dask-mpi"
 - "dask-remote"
 - "dask-submit"
 - "gemini"
 - "grabix"
 - "ipcluster"
 - "ipcontroller"
 - "ipengine"
 - "aggregate_scores_in_intervals.py"
 - "align_print_template.py"
 - "annotateBed"
 - "axt_extract_ranges.py"
 - "axt_to_fasta.py"
 - "axt_to_lav.py"
 - "axt_to_maf.py"
 - "bamToBed"
 - "bamToFastq"
 - "bed12ToBed6"
versions:
 - "0.30.2--py27h6a6cfb3_5"
description: "shpc-registry automated BioContainers addition for gemini"
config: {"url": "https://biocontainers.pro/tools/gemini", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gemini", "latest": {"0.30.2--py27h6a6cfb3_5": "sha256:373181e58cfde76f65811879a26fcc37d289c8f4d76bdc8ec72cc79d1a0a0396"}, "tags": {"0.30.2--py27h6a6cfb3_5": "sha256:373181e58cfde76f65811879a26fcc37d289c8f4d76bdc8ec72cc79d1a0a0396"}, "docker": "quay.io/biocontainers/gemini", "aliases": {"bottle.py": "/usr/local/bin/bottle.py", "dask-mpi": "/usr/local/bin/dask-mpi", "dask-remote": "/usr/local/bin/dask-remote", "dask-submit": "/usr/local/bin/dask-submit", "gemini": "/usr/local/bin/gemini", "grabix": "/usr/local/bin/grabix", "ipcluster": "/usr/local/bin/ipcluster", "ipcontroller": "/usr/local/bin/ipcontroller", "ipengine": "/usr/local/bin/ipengine", "aggregate_scores_in_intervals.py": "/usr/local/bin/aggregate_scores_in_intervals.py", "align_print_template.py": "/usr/local/bin/align_print_template.py", "annotateBed": "/usr/local/bin/annotateBed", "axt_extract_ranges.py": "/usr/local/bin/axt_extract_ranges.py", "axt_to_fasta.py": "/usr/local/bin/axt_to_fasta.py", "axt_to_lav.py": "/usr/local/bin/axt_to_lav.py", "axt_to_maf.py": "/usr/local/bin/axt_to_maf.py", "bamToBed": "/usr/local/bin/bamToBed", "bamToFastq": "/usr/local/bin/bamToFastq", "bed12ToBed6": "/usr/local/bin/bed12ToBed6"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gemini.
shpc-registry automated BioContainers addition for gemini
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gemini
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gemini:0.30.2--py27h6a6cfb3_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gemini/0.30.2--py27h6a6cfb3_5
$ module help quay.io/biocontainers/gemini/0.30.2--py27h6a6cfb3_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gemini-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gemini-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gemini-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gemini-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gemini-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gemini-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bottle.py

```bash
$ singularity exec <container> /usr/local/bin/bottle.py
$ podman run --it --rm --entrypoint /usr/local/bin/bottle.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bottle.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dask-mpi

```bash
$ singularity exec <container> /usr/local/bin/dask-mpi
$ podman run --it --rm --entrypoint /usr/local/bin/dask-mpi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dask-mpi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dask-remote

```bash
$ singularity exec <container> /usr/local/bin/dask-remote
$ podman run --it --rm --entrypoint /usr/local/bin/dask-remote   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dask-remote   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dask-submit

```bash
$ singularity exec <container> /usr/local/bin/dask-submit
$ podman run --it --rm --entrypoint /usr/local/bin/dask-submit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dask-submit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gemini

```bash
$ singularity exec <container> /usr/local/bin/gemini
$ podman run --it --rm --entrypoint /usr/local/bin/gemini   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gemini   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grabix

```bash
$ singularity exec <container> /usr/local/bin/grabix
$ podman run --it --rm --entrypoint /usr/local/bin/grabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grabix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipcluster

```bash
$ singularity exec <container> /usr/local/bin/ipcluster
$ podman run --it --rm --entrypoint /usr/local/bin/ipcluster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipcluster   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipcontroller

```bash
$ singularity exec <container> /usr/local/bin/ipcontroller
$ podman run --it --rm --entrypoint /usr/local/bin/ipcontroller   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipcontroller   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipengine

```bash
$ singularity exec <container> /usr/local/bin/ipengine
$ podman run --it --rm --entrypoint /usr/local/bin/ipengine   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipengine   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### annotateBed

```bash
$ singularity exec <container> /usr/local/bin/annotateBed
$ podman run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### bamToBed

```bash
$ singularity exec <container> /usr/local/bin/bamToBed
$ podman run --it --rm --entrypoint /usr/local/bin/bamToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamToFastq

```bash
$ singularity exec <container> /usr/local/bin/bamToFastq
$ podman run --it --rm --entrypoint /usr/local/bin/bamToFastq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamToFastq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bed12ToBed6

```bash
$ singularity exec <container> /usr/local/bin/bed12ToBed6
$ podman run --it --rm --entrypoint /usr/local/bin/bed12ToBed6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bed12ToBed6   -v ${PWD} -w ${PWD} <container> -c " $@"
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
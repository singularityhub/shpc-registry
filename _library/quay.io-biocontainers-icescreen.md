---
layout: container
name:  "quay.io/biocontainers/icescreen"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/icescreen/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/icescreen/container.yaml"
updated_at: "2025-02-26 03:05:46.375075"
latest: "1.3.2--py312h7e72e81_1"
container_url: "https://biocontainers.pro/tools/icescreen"
aliases:
 - "AUTHORS.txt"
 - "INSTALL"
 - "LICENCE.txt"
 - "LOG_public_releases"
 - "agpl-3.0.txt"
 - "icescreen"
 - "plac_runner.py"
 - "yte"
 - "docutils"
 - "metadata_conda_debug.yaml"
 - "pulptest"
 - "cbc"
 - "clp"
 - "aggregate_scores_in_intervals.py"
 - "align_print_template.py"
 - "axt_extract_ranges.py"
versions:
 - "1.0.4--py310hdfd78af_1"
 - "1.1.0--py311hdfd78af_0"
 - "1.1.1--py311hdfd78af_0"
 - "1.2.0--py310h7cba7a3_0"
 - "1.3.1--py310h7cba7a3_0"
 - "1.3.2--py310h7cba7a3_0"
 - "1.3.2--py312h7e72e81_1"
description: "shpc-registry automated BioContainers addition for icescreen"
config: {"url": "https://biocontainers.pro/tools/icescreen", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for icescreen", "latest": {"1.3.2--py312h7e72e81_1": "sha256:0608c050eb7251232a092725360ee68a9e872732d3ed3bd4fc71696e4895148b"}, "tags": {"1.0.4--py310hdfd78af_1": "sha256:f47e05529012f861315b89a6ef1fa960f4ab16a92ee65c5e750f855f3025c1cd", "1.1.0--py311hdfd78af_0": "sha256:15fe55a3e509321e3ad4d270ebd7723f7ab5c0cff814cd2550c0581b511f0a54", "1.1.1--py311hdfd78af_0": "sha256:c6ada927efc8a7e6e772f119ba8d7adee8caae0d3346fc1a904713d4be581fc4", "1.2.0--py310h7cba7a3_0": "sha256:0b8fdd2aa670d97c357a737d18620b79203a0447d654190b96d8a94ffdf9f393", "1.3.1--py310h7cba7a3_0": "sha256:c7908d1d554bdf88993cd1bd549166177dc9317bec0f658cf0a7ca574615c1a0", "1.3.2--py310h7cba7a3_0": "sha256:a2622484171dde5c87f3ae6d80988bff16760a56ce34f2f98b8c39f4d847afbe", "1.3.2--py312h7e72e81_1": "sha256:0608c050eb7251232a092725360ee68a9e872732d3ed3bd4fc71696e4895148b"}, "docker": "quay.io/biocontainers/icescreen", "aliases": {"AUTHORS.txt": "/usr/local/bin/AUTHORS.txt", "INSTALL": "/usr/local/bin/INSTALL", "LICENCE.txt": "/usr/local/bin/LICENCE.txt", "LOG_public_releases": "/usr/local/bin/LOG_public_releases", "agpl-3.0.txt": "/usr/local/bin/agpl-3.0.txt", "icescreen": "/usr/local/bin/icescreen", "plac_runner.py": "/usr/local/bin/plac_runner.py", "yte": "/usr/local/bin/yte", "docutils": "/usr/local/bin/docutils", "metadata_conda_debug.yaml": "/usr/local/bin/metadata_conda_debug.yaml", "pulptest": "/usr/local/bin/pulptest", "cbc": "/usr/local/bin/cbc", "clp": "/usr/local/bin/clp", "aggregate_scores_in_intervals.py": "/usr/local/bin/aggregate_scores_in_intervals.py", "align_print_template.py": "/usr/local/bin/align_print_template.py", "axt_extract_ranges.py": "/usr/local/bin/axt_extract_ranges.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/icescreen.
shpc-registry automated BioContainers addition for icescreen
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/icescreen
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/icescreen:1.3.2--py312h7e72e81_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/icescreen/1.3.2--py312h7e72e81_1
$ module help quay.io/biocontainers/icescreen/1.3.2--py312h7e72e81_1
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


#### plac_runner.py

```bash
$ singularity exec <container> /usr/local/bin/plac_runner.py
$ podman run --it --rm --entrypoint /usr/local/bin/plac_runner.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plac_runner.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### yte

```bash
$ singularity exec <container> /usr/local/bin/yte
$ podman run --it --rm --entrypoint /usr/local/bin/yte   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yte   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### docutils

```bash
$ singularity exec <container> /usr/local/bin/docutils
$ podman run --it --rm --entrypoint /usr/local/bin/docutils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/docutils   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metadata_conda_debug.yaml

```bash
$ singularity exec <container> /usr/local/bin/metadata_conda_debug.yaml
$ podman run --it --rm --entrypoint /usr/local/bin/metadata_conda_debug.yaml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metadata_conda_debug.yaml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pulptest

```bash
$ singularity exec <container> /usr/local/bin/pulptest
$ podman run --it --rm --entrypoint /usr/local/bin/pulptest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pulptest   -v ${PWD} -w ${PWD} <container> -c " $@"
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
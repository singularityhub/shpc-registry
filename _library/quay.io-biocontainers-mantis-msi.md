---
layout: container
name:  "quay.io/biocontainers/mantis-msi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mantis-msi/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mantis-msi/container.yaml"
updated_at: "2023-05-24 03:09:24.887303"
latest: "1.0.5--h9f5acd7_1"
container_url: "https://biocontainers.pro/tools/mantis-msi"
aliases:
 - "RepeatFinder"
 - "calculate_instability.py"
 - "defaults.py"
 - "helpers.py"
 - "kmer_count_filter.py"
 - "kmer_repeat_counter.py"
 - "mantis-msi.py"
 - "offset_finder.py"
 - "structures.py"
 - "f2py3.9"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "1.0.5--h9f5acd7_1"
description: "singularity registry hpc automated addition for mantis-msi"
config: {"url": "https://biocontainers.pro/tools/mantis-msi", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for mantis-msi", "latest": {"1.0.5--h9f5acd7_1": "sha256:3ec10ef4f1902d683b23824feed778db95dfacc6115ebeada5e50f968f05b28a"}, "tags": {"1.0.5--h9f5acd7_1": "sha256:3ec10ef4f1902d683b23824feed778db95dfacc6115ebeada5e50f968f05b28a"}, "docker": "quay.io/biocontainers/mantis-msi", "aliases": {"RepeatFinder": "/usr/local/bin/RepeatFinder", "calculate_instability.py": "/usr/local/bin/calculate_instability.py", "defaults.py": "/usr/local/bin/defaults.py", "helpers.py": "/usr/local/bin/helpers.py", "kmer_count_filter.py": "/usr/local/bin/kmer_count_filter.py", "kmer_repeat_counter.py": "/usr/local/bin/kmer_repeat_counter.py", "mantis-msi.py": "/usr/local/bin/mantis-msi.py", "offset_finder.py": "/usr/local/bin/offset_finder.py", "structures.py": "/usr/local/bin/structures.py", "f2py3.9": "/usr/local/bin/f2py3.9", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mantis-msi.
singularity registry hpc automated addition for mantis-msi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mantis-msi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mantis-msi:1.0.5--h9f5acd7_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mantis-msi/1.0.5--h9f5acd7_1
$ module help quay.io/biocontainers/mantis-msi/1.0.5--h9f5acd7_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mantis-msi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mantis-msi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mantis-msi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mantis-msi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mantis-msi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mantis-msi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### RepeatFinder

```bash
$ singularity exec <container> /usr/local/bin/RepeatFinder
$ podman run --it --rm --entrypoint /usr/local/bin/RepeatFinder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RepeatFinder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### calculate_instability.py

```bash
$ singularity exec <container> /usr/local/bin/calculate_instability.py
$ podman run --it --rm --entrypoint /usr/local/bin/calculate_instability.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/calculate_instability.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### defaults.py

```bash
$ singularity exec <container> /usr/local/bin/defaults.py
$ podman run --it --rm --entrypoint /usr/local/bin/defaults.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/defaults.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### helpers.py

```bash
$ singularity exec <container> /usr/local/bin/helpers.py
$ podman run --it --rm --entrypoint /usr/local/bin/helpers.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/helpers.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmer_count_filter.py

```bash
$ singularity exec <container> /usr/local/bin/kmer_count_filter.py
$ podman run --it --rm --entrypoint /usr/local/bin/kmer_count_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmer_count_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmer_repeat_counter.py

```bash
$ singularity exec <container> /usr/local/bin/kmer_repeat_counter.py
$ podman run --it --rm --entrypoint /usr/local/bin/kmer_repeat_counter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmer_repeat_counter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mantis-msi.py

```bash
$ singularity exec <container> /usr/local/bin/mantis-msi.py
$ podman run --it --rm --entrypoint /usr/local/bin/mantis-msi.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mantis-msi.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### offset_finder.py

```bash
$ singularity exec <container> /usr/local/bin/offset_finder.py
$ podman run --it --rm --entrypoint /usr/local/bin/offset_finder.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/offset_finder.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### structures.py

```bash
$ singularity exec <container> /usr/local/bin/structures.py
$ podman run --it --rm --entrypoint /usr/local/bin/structures.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/structures.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.9

```bash
$ singularity exec <container> /usr/local/bin/f2py3.9
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.9

```bash
$ singularity exec <container> /usr/local/bin/idle3.9
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.9

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.9
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9

```bash
$ singularity exec <container> /usr/local/bin/python3.9
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9-config

```bash
$ singularity exec <container> /usr/local/bin/python3.9-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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
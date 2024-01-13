---
layout: container
name:  "quay.io/biocontainers/bs-seeker2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bs-seeker2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bs-seeker2/container.yaml"
updated_at: "2024-01-13 02:49:26.225246"
latest: "2.1.7--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bs-seeker2"
aliases:
 - "AUTHORS"
 - "Antisense.py"
 - "FilterReads.py"
 - "RELEASE_NOTES"
 - "bs_seeker2-align.py"
 - "bs_seeker2-build.py"
 - "bs_seeker2-call_methylation.py"
 - "metadata_conda_debug.yaml"
 - "perl5.32.0"
 - "bowtie2"
 - "bowtie2-align-l"
 - "bowtie2-align-s"
 - "bowtie2-build"
 - "bowtie2-build-l"
 - "bowtie2-build-s"
 - "bowtie2-inspect"
 - "bowtie2-inspect-l"
versions:
 - "2.1.7--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for bs-seeker2"
config: {"url": "https://biocontainers.pro/tools/bs-seeker2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bs-seeker2", "latest": {"2.1.7--hdfd78af_1": "sha256:5b4e6e2c7f482d93afb2e18ede213f08c0da97a414e6d0d691c03996772b60ef"}, "tags": {"2.1.7--hdfd78af_1": "sha256:5b4e6e2c7f482d93afb2e18ede213f08c0da97a414e6d0d691c03996772b60ef"}, "docker": "quay.io/biocontainers/bs-seeker2", "aliases": {"AUTHORS": "/usr/local/bin/AUTHORS", "Antisense.py": "/usr/local/bin/Antisense.py", "FilterReads.py": "/usr/local/bin/FilterReads.py", "RELEASE_NOTES": "/usr/local/bin/RELEASE_NOTES", "bs_seeker2-align.py": "/usr/local/bin/bs_seeker2-align.py", "bs_seeker2-build.py": "/usr/local/bin/bs_seeker2-build.py", "bs_seeker2-call_methylation.py": "/usr/local/bin/bs_seeker2-call_methylation.py", "metadata_conda_debug.yaml": "/usr/local/bin/metadata_conda_debug.yaml", "perl5.32.0": "/usr/local/bin/perl5.32.0", "bowtie2": "/usr/local/bin/bowtie2", "bowtie2-align-l": "/usr/local/bin/bowtie2-align-l", "bowtie2-align-s": "/usr/local/bin/bowtie2-align-s", "bowtie2-build": "/usr/local/bin/bowtie2-build", "bowtie2-build-l": "/usr/local/bin/bowtie2-build-l", "bowtie2-build-s": "/usr/local/bin/bowtie2-build-s", "bowtie2-inspect": "/usr/local/bin/bowtie2-inspect", "bowtie2-inspect-l": "/usr/local/bin/bowtie2-inspect-l"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bs-seeker2.
shpc-registry automated BioContainers addition for bs-seeker2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bs-seeker2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bs-seeker2:2.1.7--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bs-seeker2/2.1.7--hdfd78af_1
$ module help quay.io/biocontainers/bs-seeker2/2.1.7--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bs-seeker2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bs-seeker2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bs-seeker2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bs-seeker2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bs-seeker2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bs-seeker2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### AUTHORS

```bash
$ singularity exec <container> /usr/local/bin/AUTHORS
$ podman run --it --rm --entrypoint /usr/local/bin/AUTHORS   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AUTHORS   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Antisense.py

```bash
$ singularity exec <container> /usr/local/bin/Antisense.py
$ podman run --it --rm --entrypoint /usr/local/bin/Antisense.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Antisense.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FilterReads.py

```bash
$ singularity exec <container> /usr/local/bin/FilterReads.py
$ podman run --it --rm --entrypoint /usr/local/bin/FilterReads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FilterReads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RELEASE_NOTES

```bash
$ singularity exec <container> /usr/local/bin/RELEASE_NOTES
$ podman run --it --rm --entrypoint /usr/local/bin/RELEASE_NOTES   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RELEASE_NOTES   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bs_seeker2-align.py

```bash
$ singularity exec <container> /usr/local/bin/bs_seeker2-align.py
$ podman run --it --rm --entrypoint /usr/local/bin/bs_seeker2-align.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bs_seeker2-align.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bs_seeker2-build.py

```bash
$ singularity exec <container> /usr/local/bin/bs_seeker2-build.py
$ podman run --it --rm --entrypoint /usr/local/bin/bs_seeker2-build.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bs_seeker2-build.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bs_seeker2-call_methylation.py

```bash
$ singularity exec <container> /usr/local/bin/bs_seeker2-call_methylation.py
$ podman run --it --rm --entrypoint /usr/local/bin/bs_seeker2-call_methylation.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bs_seeker2-call_methylation.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metadata_conda_debug.yaml

```bash
$ singularity exec <container> /usr/local/bin/metadata_conda_debug.yaml
$ podman run --it --rm --entrypoint /usr/local/bin/metadata_conda_debug.yaml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metadata_conda_debug.yaml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.32.0

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.0
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2

```bash
$ singularity exec <container> /usr/local/bin/bowtie2
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-align-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-align-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-align-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-align-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-build

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-build
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-build-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-build-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-build-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-build-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-build-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-build-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-inspect

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-inspect
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-inspect-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-inspect-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-inspect-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-inspect-l   -v ${PWD} -w ${PWD} <container> -c " $@"
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
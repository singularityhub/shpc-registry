---
layout: container
name:  "quay.io/biocontainers/dkfz-bias-filter"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dkfz-bias-filter/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/dkfz-bias-filter/container.yaml"
updated_at: "2022-10-27 01:11:32.511695"
latest: "1.2.3a--hdfd78af_9"
container_url: "https://biocontainers.pro/tools/dkfz-bias-filter"
aliases:
 - "dkfzbiasfilter.py"
 - "dkfzbiasfilter_summarize.py"
versions:
 - "1.2.3a--hdfd78af_9"
description: "shpc-registry automated BioContainers addition for dkfz-bias-filter"
config: {"url": "https://biocontainers.pro/tools/dkfz-bias-filter", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dkfz-bias-filter", "latest": {"1.2.3a--hdfd78af_9": "sha256:219bcd8dbcd6d178cca909cc2ab100f8cbfa5cc432bbab4d6578162acca2cc1f"}, "tags": {"1.2.3a--hdfd78af_9": "sha256:219bcd8dbcd6d178cca909cc2ab100f8cbfa5cc432bbab4d6578162acca2cc1f"}, "docker": "quay.io/biocontainers/dkfz-bias-filter", "aliases": {"dkfzbiasfilter.py": "/usr/local/bin/dkfzbiasfilter.py", "dkfzbiasfilter_summarize.py": "/usr/local/bin/dkfzbiasfilter_summarize.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dkfz-bias-filter.
shpc-registry automated BioContainers addition for dkfz-bias-filter
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dkfz-bias-filter
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dkfz-bias-filter:1.2.3a--hdfd78af_9
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dkfz-bias-filter/1.2.3a--hdfd78af_9
$ module help quay.io/biocontainers/dkfz-bias-filter/1.2.3a--hdfd78af_9
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dkfz-bias-filter-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dkfz-bias-filter-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dkfz-bias-filter-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dkfz-bias-filter-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dkfz-bias-filter-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dkfz-bias-filter-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dkfzbiasfilter.py

```bash
$ singularity exec <container> /usr/local/bin/dkfzbiasfilter.py
$ podman run --it --rm --entrypoint /usr/local/bin/dkfzbiasfilter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dkfzbiasfilter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dkfzbiasfilter_summarize.py

```bash
$ singularity exec <container> /usr/local/bin/dkfzbiasfilter_summarize.py
$ podman run --it --rm --entrypoint /usr/local/bin/dkfzbiasfilter_summarize.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dkfzbiasfilter_summarize.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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
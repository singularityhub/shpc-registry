---
layout: container
name:  "quay.io/biocontainers/variabel"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/variabel/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/variabel/container.yaml"
updated_at: "2022-10-27 00:18:52.455358"
latest: "1.0.0--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/variabel"
aliases:
 - "lofreq2_indel_ovlp.py"
 - "lofreq2_vcfplot.py"
 - "variabel"
versions:
 - "1.0.0--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for variabel"
config: {"url": "https://biocontainers.pro/tools/variabel", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for variabel", "latest": {"1.0.0--hdfd78af_0": "sha256:f0a7bded8d9eb27c251d8dd4d06785c5d4e2558f083b24fd55156d7d7d55e661"}, "tags": {"1.0.0--hdfd78af_0": "sha256:f0a7bded8d9eb27c251d8dd4d06785c5d4e2558f083b24fd55156d7d7d55e661"}, "docker": "quay.io/biocontainers/variabel", "aliases": {"lofreq2_indel_ovlp.py": "/usr/local/bin/lofreq2_indel_ovlp.py", "lofreq2_vcfplot.py": "/usr/local/bin/lofreq2_vcfplot.py", "variabel": "/usr/local/bin/variabel"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/variabel.
shpc-registry automated BioContainers addition for variabel
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/variabel
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/variabel:1.0.0--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/variabel/1.0.0--hdfd78af_0
$ module help quay.io/biocontainers/variabel/1.0.0--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### variabel-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### variabel-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### variabel-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### variabel-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### variabel-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### variabel-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### lofreq2_indel_ovlp.py

```bash
$ singularity exec <container> /usr/local/bin/lofreq2_indel_ovlp.py
$ podman run --it --rm --entrypoint /usr/local/bin/lofreq2_indel_ovlp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lofreq2_indel_ovlp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lofreq2_vcfplot.py

```bash
$ singularity exec <container> /usr/local/bin/lofreq2_vcfplot.py
$ podman run --it --rm --entrypoint /usr/local/bin/lofreq2_vcfplot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lofreq2_vcfplot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### variabel

```bash
$ singularity exec <container> /usr/local/bin/variabel
$ podman run --it --rm --entrypoint /usr/local/bin/variabel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/variabel   -v ${PWD} -w ${PWD} <container> -c " $@"
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
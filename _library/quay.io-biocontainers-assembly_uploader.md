---
layout: container
name:  "quay.io/biocontainers/assembly_uploader"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/assembly_uploader/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/assembly_uploader/container.yaml"
updated_at: "2025-11-08 03:13:19.727445"
latest: "1.3.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/assembly_uploader"
aliases:
 - "assembly_manifest"
 - "release_study"
 - "study_xmls"
 - "submit_study"
 - "idle3.14"
 - "pydoc3.14"
 - "python3.14"
 - "python3.14-config"
 - "normalizer"
versions:
 - "1.3.2--pyhdfd78af_0"
description: "singularity registry hpc automated addition for assembly_uploader"
config: {"url": "https://biocontainers.pro/tools/assembly_uploader", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for assembly_uploader", "latest": {"1.3.2--pyhdfd78af_0": "sha256:511f296f5d3620abf95384b1dd33b42b9a4efce64ee86af4516a2d9413b8d637"}, "tags": {"1.3.2--pyhdfd78af_0": "sha256:511f296f5d3620abf95384b1dd33b42b9a4efce64ee86af4516a2d9413b8d637"}, "docker": "quay.io/biocontainers/assembly_uploader", "aliases": {"assembly_manifest": "/usr/local/bin/assembly_manifest", "release_study": "/usr/local/bin/release_study", "study_xmls": "/usr/local/bin/study_xmls", "submit_study": "/usr/local/bin/submit_study", "idle3.14": "/usr/local/bin/idle3.14", "pydoc3.14": "/usr/local/bin/pydoc3.14", "python3.14": "/usr/local/bin/python3.14", "python3.14-config": "/usr/local/bin/python3.14-config", "normalizer": "/usr/local/bin/normalizer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/assembly_uploader.
singularity registry hpc automated addition for assembly_uploader
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/assembly_uploader
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/assembly_uploader:1.3.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/assembly_uploader/1.3.2--pyhdfd78af_0
$ module help quay.io/biocontainers/assembly_uploader/1.3.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### assembly_uploader-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### assembly_uploader-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### assembly_uploader-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### assembly_uploader-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### assembly_uploader-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### assembly_uploader-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### assembly_manifest

```bash
$ singularity exec <container> /usr/local/bin/assembly_manifest
$ podman run --it --rm --entrypoint /usr/local/bin/assembly_manifest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/assembly_manifest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### release_study

```bash
$ singularity exec <container> /usr/local/bin/release_study
$ podman run --it --rm --entrypoint /usr/local/bin/release_study   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/release_study   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### study_xmls

```bash
$ singularity exec <container> /usr/local/bin/study_xmls
$ podman run --it --rm --entrypoint /usr/local/bin/study_xmls   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/study_xmls   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### submit_study

```bash
$ singularity exec <container> /usr/local/bin/submit_study
$ podman run --it --rm --entrypoint /usr/local/bin/submit_study   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/submit_study   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.14

```bash
$ singularity exec <container> /usr/local/bin/idle3.14
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.14

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.14
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14

```bash
$ singularity exec <container> /usr/local/bin/python3.14
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14-config

```bash
$ singularity exec <container> /usr/local/bin/python3.14-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
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
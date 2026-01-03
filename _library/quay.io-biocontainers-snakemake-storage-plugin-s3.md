---
layout: container
name:  "quay.io/biocontainers/snakemake-storage-plugin-s3"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/snakemake-storage-plugin-s3/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/snakemake-storage-plugin-s3/container.yaml"
updated_at: "2026-01-03 04:07:10.065391"
latest: "0.3.6--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/snakemake-storage-plugin-s3"
aliases:
 - "2to3-3.12"
 - "idle3.12"
 - "pydoc3.12"
 - "python3.12"
 - "python3.12-config"
 - "jp.py"
versions:
 - "0.2.8--pyhdfd78af_1"
 - "0.2.10--pyhdfd78af_0"
 - "0.2.11--pyhdfd78af_0"
 - "0.2.12--pyhdfd78af_0"
 - "0.2.13--pyhdfd78af_0"
 - "0.3.3--pyhdfd78af_0"
 - "0.3.4--pyhdfd78af_0"
 - "0.3.6--pyhdfd78af_0"
description: "singularity registry hpc automated addition for snakemake-storage-plugin-s3"
config: {"url": "https://biocontainers.pro/tools/snakemake-storage-plugin-s3", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for snakemake-storage-plugin-s3", "latest": {"0.3.6--pyhdfd78af_0": "sha256:45cdecdad79f038bfe55fbfab008f1cde520e30e4fb6d360fe62def4400bfc06"}, "tags": {"0.2.8--pyhdfd78af_1": "sha256:12cd4ef702fc9ad87d34f8b9d2948981834a9f25667f3e18c4e41187757a5912", "0.2.10--pyhdfd78af_0": "sha256:c44f5aa92defa07728ebc0cf64218b367b43e5b9b964368ce58837cf12ff7b74", "0.2.11--pyhdfd78af_0": "sha256:2ce6ac3c565f2c00d57f88d6a5bd3f53108b925397f30c49e57da38f021d0293", "0.2.12--pyhdfd78af_0": "sha256:e51dc3d5f5337a8df30f9c2f3aac800aade5017a0550a35ee8fd3100fc4fac29", "0.2.13--pyhdfd78af_0": "sha256:64508604e605da235e64f9d73bcdc79e27694348cadeaed365595c20b0f19ab6", "0.3.3--pyhdfd78af_0": "sha256:75a145b7bb6c763ebda48a379b2927b8ddba6adfeb4f76c7cfa6cf69b38db1fc", "0.3.4--pyhdfd78af_0": "sha256:bf5f5e95d6ccff9d3837b383e575a8d70194da1394d2599cfda9d91f9a4e5ab0", "0.3.6--pyhdfd78af_0": "sha256:45cdecdad79f038bfe55fbfab008f1cde520e30e4fb6d360fe62def4400bfc06"}, "docker": "quay.io/biocontainers/snakemake-storage-plugin-s3", "aliases": {"2to3-3.12": "/usr/local/bin/2to3-3.12", "idle3.12": "/usr/local/bin/idle3.12", "pydoc3.12": "/usr/local/bin/pydoc3.12", "python3.12": "/usr/local/bin/python3.12", "python3.12-config": "/usr/local/bin/python3.12-config", "jp.py": "/usr/local/bin/jp.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/snakemake-storage-plugin-s3.
singularity registry hpc automated addition for snakemake-storage-plugin-s3
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/snakemake-storage-plugin-s3
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/snakemake-storage-plugin-s3:0.3.6--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/snakemake-storage-plugin-s3/0.3.6--pyhdfd78af_0
$ module help quay.io/biocontainers/snakemake-storage-plugin-s3/0.3.6--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### snakemake-storage-plugin-s3-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### snakemake-storage-plugin-s3-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### snakemake-storage-plugin-s3-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### snakemake-storage-plugin-s3-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### snakemake-storage-plugin-s3-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### snakemake-storage-plugin-s3-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 2to3-3.12

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.12
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.12

```bash
$ singularity exec <container> /usr/local/bin/idle3.12
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.12

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.12
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12

```bash
$ singularity exec <container> /usr/local/bin/python3.12
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12-config

```bash
$ singularity exec <container> /usr/local/bin/python3.12-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jp.py

```bash
$ singularity exec <container> /usr/local/bin/jp.py
$ podman run --it --rm --entrypoint /usr/local/bin/jp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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
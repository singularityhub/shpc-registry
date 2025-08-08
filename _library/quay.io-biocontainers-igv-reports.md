---
layout: container
name:  "quay.io/biocontainers/igv-reports"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/igv-reports/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/igv-reports/container.yaml"
updated_at: "2025-08-08 04:13:01.103024"
latest: "1.15.1--pyh7e72e81_0"
container_url: "https://biocontainers.pro/tools/igv-reports"
aliases:
 - "create_datauri"
 - "create_report"
 - "normalizer"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.1"
 - "python3.10"
 - "python3.10-config"
versions:
 - "1.6.1--pyh7cba7a3_0"
 - "1.7.0--pyh7cba7a3_0"
 - "1.8.0--pyh7cba7a3_0"
 - "1.9.1--pyh7cba7a3_0"
 - "1.8.1--pyh7cba7a3_0"
 - "1.10.0--pyh7cba7a3_0"
 - "1.12.0--pyh7cba7a3_0"
 - "1.11.0--pyh7cba7a3_0"
 - "1.13.0--pyh7e72e81_0"
 - "1.14.1--pyh7e72e81_0"
 - "1.15.1--pyh7e72e81_0"
description: "shpc-registry automated BioContainers addition for igv-reports"
config: {"url": "https://biocontainers.pro/tools/igv-reports", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for igv-reports", "latest": {"1.15.1--pyh7e72e81_0": "sha256:786533526131817fe126fdb86308bcc6b63079bd3d8eb4c6478a0acc4b229b08"}, "tags": {"1.6.1--pyh7cba7a3_0": "sha256:5f8e40f84d3398f243d1cea959802752e8d8f54686dba4a389144746e69b1294", "1.7.0--pyh7cba7a3_0": "sha256:2f5b08c6d82467e1cd6140ecd1b496b82bdb094e864301a281b4d4858df74137", "1.8.0--pyh7cba7a3_0": "sha256:f8d6f43c4c97bc13788d206e67e42dad5e2564edba04413699793f9a15ef5901", "1.9.1--pyh7cba7a3_0": "sha256:c52ca010e61b0804af10f87e2c32665cc453b6dd7b6899c15ee1ee0a9c237138", "1.8.1--pyh7cba7a3_0": "sha256:992c03efa36ffbda894fc3b98393c613a7a24e5929df1bdde6b980dd8ba36d9a", "1.10.0--pyh7cba7a3_0": "sha256:7cac752e99fc43fdc788d8f23afe3a7a4c67dd6c7852d731c156bc077388ea6c", "1.12.0--pyh7cba7a3_0": "sha256:52c64065cd8229cbe19520b44df78cdcd920bc44b5a1d5ade705a8db6c3cfcce", "1.11.0--pyh7cba7a3_0": "sha256:5dd9e79f6ddbbfc9e7885d4e860a4c7570bbd62cbe7dfd3991f37d5e8e6d2b60", "1.13.0--pyh7e72e81_0": "sha256:113d38018b305aaa6af2161011b91ae342d4e63a306aad4a68ad5646af830a65", "1.14.1--pyh7e72e81_0": "sha256:e15f1fdfb25e9c74e2c74468be9f3d4c51352ddd9020b69a10660c67908115d5", "1.15.1--pyh7e72e81_0": "sha256:786533526131817fe126fdb86308bcc6b63079bd3d8eb4c6478a0acc4b229b08"}, "docker": "quay.io/biocontainers/igv-reports", "aliases": {"create_datauri": "/usr/local/bin/create_datauri", "create_report": "/usr/local/bin/create_report", "normalizer": "/usr/local/bin/normalizer", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.1": "/usr/local/bin/python3.1", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/igv-reports.
shpc-registry automated BioContainers addition for igv-reports
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/igv-reports
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/igv-reports:1.15.1--pyh7e72e81_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/igv-reports/1.15.1--pyh7e72e81_0
$ module help quay.io/biocontainers/igv-reports/1.15.1--pyh7e72e81_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### igv-reports-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### igv-reports-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### igv-reports-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### igv-reports-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### igv-reports-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### igv-reports-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### create_datauri

```bash
$ singularity exec <container> /usr/local/bin/create_datauri
$ podman run --it --rm --entrypoint /usr/local/bin/create_datauri   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/create_datauri   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### create_report

```bash
$ singularity exec <container> /usr/local/bin/create_report
$ podman run --it --rm --entrypoint /usr/local/bin/create_report   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/create_report   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.10

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.10
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10

```bash
$ singularity exec <container> /usr/local/bin/python3.10
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10-config

```bash
$ singularity exec <container> /usr/local/bin/python3.10-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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
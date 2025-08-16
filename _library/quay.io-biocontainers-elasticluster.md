---
layout: container
name:  "quay.io/biocontainers/elasticluster"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/elasticluster/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/elasticluster/container.yaml"
updated_at: "2025-08-16 03:25:28.216750"
latest: "0.1.3bcbio--py27_12"
container_url: "https://biocontainers.pro/tools/elasticluster"
aliases:
 - "ansible"
 - "ansible-doc"
 - "ansible-galaxy"
 - "ansible-playbook"
 - "ansible-pull"
 - "ansible-vault"
 - "elasticluster"
 - "gflags2man.py"
 - "pyrsa-decrypt-bigfile"
 - "pyrsa-encrypt-bigfile"
 - "asadmin"
 - "bundle_image"
 - "cfadmin"
 - "cq"
 - "cwutil"
 - "dynamodb_dump"
 - "dynamodb_load"
 - "elbadmin"
versions:
 - "0.1.3bcbio--py27_12"
description: "shpc-registry automated BioContainers addition for elasticluster"
config: {"url": "https://biocontainers.pro/tools/elasticluster", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for elasticluster", "latest": {"0.1.3bcbio--py27_12": "sha256:ba6b826c888a9cb273b2591d115d200a55b5781d14b2b32be08521b10718e6d1"}, "tags": {"0.1.3bcbio--py27_12": "sha256:ba6b826c888a9cb273b2591d115d200a55b5781d14b2b32be08521b10718e6d1"}, "docker": "quay.io/biocontainers/elasticluster", "aliases": {"ansible": "/usr/local/bin/ansible", "ansible-doc": "/usr/local/bin/ansible-doc", "ansible-galaxy": "/usr/local/bin/ansible-galaxy", "ansible-playbook": "/usr/local/bin/ansible-playbook", "ansible-pull": "/usr/local/bin/ansible-pull", "ansible-vault": "/usr/local/bin/ansible-vault", "elasticluster": "/usr/local/bin/elasticluster", "gflags2man.py": "/usr/local/bin/gflags2man.py", "pyrsa-decrypt-bigfile": "/usr/local/bin/pyrsa-decrypt-bigfile", "pyrsa-encrypt-bigfile": "/usr/local/bin/pyrsa-encrypt-bigfile", "asadmin": "/usr/local/bin/asadmin", "bundle_image": "/usr/local/bin/bundle_image", "cfadmin": "/usr/local/bin/cfadmin", "cq": "/usr/local/bin/cq", "cwutil": "/usr/local/bin/cwutil", "dynamodb_dump": "/usr/local/bin/dynamodb_dump", "dynamodb_load": "/usr/local/bin/dynamodb_load", "elbadmin": "/usr/local/bin/elbadmin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/elasticluster.
shpc-registry automated BioContainers addition for elasticluster
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/elasticluster
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/elasticluster:0.1.3bcbio--py27_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/elasticluster/0.1.3bcbio--py27_12
$ module help quay.io/biocontainers/elasticluster/0.1.3bcbio--py27_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### elasticluster-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### elasticluster-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### elasticluster-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### elasticluster-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### elasticluster-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### elasticluster-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ansible

```bash
$ singularity exec <container> /usr/local/bin/ansible
$ podman run --it --rm --entrypoint /usr/local/bin/ansible   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ansible   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ansible-doc

```bash
$ singularity exec <container> /usr/local/bin/ansible-doc
$ podman run --it --rm --entrypoint /usr/local/bin/ansible-doc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ansible-doc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ansible-galaxy

```bash
$ singularity exec <container> /usr/local/bin/ansible-galaxy
$ podman run --it --rm --entrypoint /usr/local/bin/ansible-galaxy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ansible-galaxy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ansible-playbook

```bash
$ singularity exec <container> /usr/local/bin/ansible-playbook
$ podman run --it --rm --entrypoint /usr/local/bin/ansible-playbook   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ansible-playbook   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ansible-pull

```bash
$ singularity exec <container> /usr/local/bin/ansible-pull
$ podman run --it --rm --entrypoint /usr/local/bin/ansible-pull   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ansible-pull   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ansible-vault

```bash
$ singularity exec <container> /usr/local/bin/ansible-vault
$ podman run --it --rm --entrypoint /usr/local/bin/ansible-vault   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ansible-vault   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elasticluster

```bash
$ singularity exec <container> /usr/local/bin/elasticluster
$ podman run --it --rm --entrypoint /usr/local/bin/elasticluster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elasticluster   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gflags2man.py

```bash
$ singularity exec <container> /usr/local/bin/gflags2man.py
$ podman run --it --rm --entrypoint /usr/local/bin/gflags2man.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gflags2man.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrsa-decrypt-bigfile

```bash
$ singularity exec <container> /usr/local/bin/pyrsa-decrypt-bigfile
$ podman run --it --rm --entrypoint /usr/local/bin/pyrsa-decrypt-bigfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrsa-decrypt-bigfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrsa-encrypt-bigfile

```bash
$ singularity exec <container> /usr/local/bin/pyrsa-encrypt-bigfile
$ podman run --it --rm --entrypoint /usr/local/bin/pyrsa-encrypt-bigfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrsa-encrypt-bigfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asadmin

```bash
$ singularity exec <container> /usr/local/bin/asadmin
$ podman run --it --rm --entrypoint /usr/local/bin/asadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bundle_image

```bash
$ singularity exec <container> /usr/local/bin/bundle_image
$ podman run --it --rm --entrypoint /usr/local/bin/bundle_image   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bundle_image   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cfadmin

```bash
$ singularity exec <container> /usr/local/bin/cfadmin
$ podman run --it --rm --entrypoint /usr/local/bin/cfadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cfadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cq

```bash
$ singularity exec <container> /usr/local/bin/cq
$ podman run --it --rm --entrypoint /usr/local/bin/cq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cwutil

```bash
$ singularity exec <container> /usr/local/bin/cwutil
$ podman run --it --rm --entrypoint /usr/local/bin/cwutil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cwutil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dynamodb_dump

```bash
$ singularity exec <container> /usr/local/bin/dynamodb_dump
$ podman run --it --rm --entrypoint /usr/local/bin/dynamodb_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dynamodb_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dynamodb_load

```bash
$ singularity exec <container> /usr/local/bin/dynamodb_load
$ podman run --it --rm --entrypoint /usr/local/bin/dynamodb_load   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dynamodb_load   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elbadmin

```bash
$ singularity exec <container> /usr/local/bin/elbadmin
$ podman run --it --rm --entrypoint /usr/local/bin/elbadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elbadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
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
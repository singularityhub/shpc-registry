---
layout: container
name:  "quay.io/biocontainers/pangolin"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pangolin/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pangolin/container.yaml"
updated_at: "2023-08-10 03:48:04.233225"
latest: "4.0.3--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/pangolin"
aliases:
 - "constellations"
 - "extract_definitions.py"
 - "faToVcf"
 - "fido2-assert"
 - "fido2-cred"
 - "fido2-token"
 - "git-lfs"
 - "gofasta"
 - "matOptimize"
 - "matUtils"
 - "pangolearn.smk"
 - "pangolin"
 - "pangolin_data"
 - "preprocessing.smk"
 - "ripples"
 - "scorpio"
 - "scp"
 - "sftp"
 - "ssh"
 - "ssh-add"
 - "ssh-agent"
 - "ssh-keygen"
 - "ssh-keyscan"
 - "sshd"
 - "type_constellations.py"
 - "usher"
 - "usher.smk"
 - "oshCC"
 - "oshc++"
 - "oshcxx"
 - "shmemCC"
 - "shmemc++"
 - "shmemcxx"
 - "oshcc"
 - "oshfort"
 - "oshmem_info"
 - "oshrun"
versions:
 - "4.0.3--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for pangolin"
config: {"url": "https://biocontainers.pro/tools/pangolin", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pangolin", "latest": {"4.0.3--pyhdfd78af_0": "sha256:c997d652643071694f8392c0a787a4b24a1bc3c5125b606f123a931f24ac833c"}, "tags": {"4.0.3--pyhdfd78af_0": "sha256:c997d652643071694f8392c0a787a4b24a1bc3c5125b606f123a931f24ac833c"}, "docker": "quay.io/biocontainers/pangolin", "aliases": {"constellations": "/usr/local/bin/constellations", "extract_definitions.py": "/usr/local/bin/extract_definitions.py", "faToVcf": "/usr/local/bin/faToVcf", "fido2-assert": "/usr/local/bin/fido2-assert", "fido2-cred": "/usr/local/bin/fido2-cred", "fido2-token": "/usr/local/bin/fido2-token", "git-lfs": "/usr/local/bin/git-lfs", "gofasta": "/usr/local/bin/gofasta", "matOptimize": "/usr/local/bin/matOptimize", "matUtils": "/usr/local/bin/matUtils", "pangolearn.smk": "/usr/local/bin/pangolearn.smk", "pangolin": "/usr/local/bin/pangolin", "pangolin_data": "/usr/local/bin/pangolin_data", "preprocessing.smk": "/usr/local/bin/preprocessing.smk", "ripples": "/usr/local/bin/ripples", "scorpio": "/usr/local/bin/scorpio", "scp": "/usr/local/bin/scp", "sftp": "/usr/local/bin/sftp", "ssh": "/usr/local/bin/ssh", "ssh-add": "/usr/local/bin/ssh-add", "ssh-agent": "/usr/local/bin/ssh-agent", "ssh-keygen": "/usr/local/bin/ssh-keygen", "ssh-keyscan": "/usr/local/bin/ssh-keyscan", "sshd": "/usr/local/bin/sshd", "type_constellations.py": "/usr/local/bin/type_constellations.py", "usher": "/usr/local/bin/usher", "usher.smk": "/usr/local/bin/usher.smk", "oshCC": "/usr/local/bin/oshCC", "oshc++": "/usr/local/bin/oshc++", "oshcxx": "/usr/local/bin/oshcxx", "shmemCC": "/usr/local/bin/shmemCC", "shmemc++": "/usr/local/bin/shmemc++", "shmemcxx": "/usr/local/bin/shmemcxx", "oshcc": "/usr/local/bin/oshcc", "oshfort": "/usr/local/bin/oshfort", "oshmem_info": "/usr/local/bin/oshmem_info", "oshrun": "/usr/local/bin/oshrun"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pangolin.
shpc-registry automated BioContainers addition for pangolin
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pangolin
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pangolin:4.0.3--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pangolin/4.0.3--pyhdfd78af_0
$ module help quay.io/biocontainers/pangolin/4.0.3--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pangolin-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pangolin-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pangolin-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pangolin-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pangolin-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pangolin-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### constellations

```bash
$ singularity exec <container> /usr/local/bin/constellations
$ podman run --it --rm --entrypoint /usr/local/bin/constellations   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/constellations   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_definitions.py

```bash
$ singularity exec <container> /usr/local/bin/extract_definitions.py
$ podman run --it --rm --entrypoint /usr/local/bin/extract_definitions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_definitions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### faToVcf

```bash
$ singularity exec <container> /usr/local/bin/faToVcf
$ podman run --it --rm --entrypoint /usr/local/bin/faToVcf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faToVcf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fido2-assert

```bash
$ singularity exec <container> /usr/local/bin/fido2-assert
$ podman run --it --rm --entrypoint /usr/local/bin/fido2-assert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fido2-assert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fido2-cred

```bash
$ singularity exec <container> /usr/local/bin/fido2-cred
$ podman run --it --rm --entrypoint /usr/local/bin/fido2-cred   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fido2-cred   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fido2-token

```bash
$ singularity exec <container> /usr/local/bin/fido2-token
$ podman run --it --rm --entrypoint /usr/local/bin/fido2-token   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fido2-token   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git-lfs

```bash
$ singularity exec <container> /usr/local/bin/git-lfs
$ podman run --it --rm --entrypoint /usr/local/bin/git-lfs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/git-lfs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gofasta

```bash
$ singularity exec <container> /usr/local/bin/gofasta
$ podman run --it --rm --entrypoint /usr/local/bin/gofasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gofasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### matOptimize

```bash
$ singularity exec <container> /usr/local/bin/matOptimize
$ podman run --it --rm --entrypoint /usr/local/bin/matOptimize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/matOptimize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### matUtils

```bash
$ singularity exec <container> /usr/local/bin/matUtils
$ podman run --it --rm --entrypoint /usr/local/bin/matUtils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/matUtils   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pangolearn.smk

```bash
$ singularity exec <container> /usr/local/bin/pangolearn.smk
$ podman run --it --rm --entrypoint /usr/local/bin/pangolearn.smk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pangolearn.smk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pangolin

```bash
$ singularity exec <container> /usr/local/bin/pangolin
$ podman run --it --rm --entrypoint /usr/local/bin/pangolin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pangolin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pangolin_data

```bash
$ singularity exec <container> /usr/local/bin/pangolin_data
$ podman run --it --rm --entrypoint /usr/local/bin/pangolin_data   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pangolin_data   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### preprocessing.smk

```bash
$ singularity exec <container> /usr/local/bin/preprocessing.smk
$ podman run --it --rm --entrypoint /usr/local/bin/preprocessing.smk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/preprocessing.smk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ripples

```bash
$ singularity exec <container> /usr/local/bin/ripples
$ podman run --it --rm --entrypoint /usr/local/bin/ripples   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ripples   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scorpio

```bash
$ singularity exec <container> /usr/local/bin/scorpio
$ podman run --it --rm --entrypoint /usr/local/bin/scorpio   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scorpio   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scp

```bash
$ singularity exec <container> /usr/local/bin/scp
$ podman run --it --rm --entrypoint /usr/local/bin/scp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sftp

```bash
$ singularity exec <container> /usr/local/bin/sftp
$ podman run --it --rm --entrypoint /usr/local/bin/sftp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sftp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ssh

```bash
$ singularity exec <container> /usr/local/bin/ssh
$ podman run --it --rm --entrypoint /usr/local/bin/ssh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ssh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ssh-add

```bash
$ singularity exec <container> /usr/local/bin/ssh-add
$ podman run --it --rm --entrypoint /usr/local/bin/ssh-add   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ssh-add   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ssh-agent

```bash
$ singularity exec <container> /usr/local/bin/ssh-agent
$ podman run --it --rm --entrypoint /usr/local/bin/ssh-agent   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ssh-agent   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ssh-keygen

```bash
$ singularity exec <container> /usr/local/bin/ssh-keygen
$ podman run --it --rm --entrypoint /usr/local/bin/ssh-keygen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ssh-keygen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ssh-keyscan

```bash
$ singularity exec <container> /usr/local/bin/ssh-keyscan
$ podman run --it --rm --entrypoint /usr/local/bin/ssh-keyscan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ssh-keyscan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sshd

```bash
$ singularity exec <container> /usr/local/bin/sshd
$ podman run --it --rm --entrypoint /usr/local/bin/sshd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sshd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### type_constellations.py

```bash
$ singularity exec <container> /usr/local/bin/type_constellations.py
$ podman run --it --rm --entrypoint /usr/local/bin/type_constellations.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/type_constellations.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### usher

```bash
$ singularity exec <container> /usr/local/bin/usher
$ podman run --it --rm --entrypoint /usr/local/bin/usher   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/usher   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### usher.smk

```bash
$ singularity exec <container> /usr/local/bin/usher.smk
$ podman run --it --rm --entrypoint /usr/local/bin/usher.smk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/usher.smk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oshCC

```bash
$ singularity exec <container> /usr/local/bin/oshCC
$ podman run --it --rm --entrypoint /usr/local/bin/oshCC   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oshCC   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oshc++

```bash
$ singularity exec <container> /usr/local/bin/oshc++
$ podman run --it --rm --entrypoint /usr/local/bin/oshc++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oshc++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oshcxx

```bash
$ singularity exec <container> /usr/local/bin/oshcxx
$ podman run --it --rm --entrypoint /usr/local/bin/oshcxx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oshcxx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shmemCC

```bash
$ singularity exec <container> /usr/local/bin/shmemCC
$ podman run --it --rm --entrypoint /usr/local/bin/shmemCC   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shmemCC   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shmemc++

```bash
$ singularity exec <container> /usr/local/bin/shmemc++
$ podman run --it --rm --entrypoint /usr/local/bin/shmemc++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shmemc++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shmemcxx

```bash
$ singularity exec <container> /usr/local/bin/shmemcxx
$ podman run --it --rm --entrypoint /usr/local/bin/shmemcxx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shmemcxx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oshcc

```bash
$ singularity exec <container> /usr/local/bin/oshcc
$ podman run --it --rm --entrypoint /usr/local/bin/oshcc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oshcc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oshfort

```bash
$ singularity exec <container> /usr/local/bin/oshfort
$ podman run --it --rm --entrypoint /usr/local/bin/oshfort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oshfort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oshmem_info

```bash
$ singularity exec <container> /usr/local/bin/oshmem_info
$ podman run --it --rm --entrypoint /usr/local/bin/oshmem_info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oshmem_info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oshrun

```bash
$ singularity exec <container> /usr/local/bin/oshrun
$ podman run --it --rm --entrypoint /usr/local/bin/oshrun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oshrun   -v ${PWD} -w ${PWD} <container> -c " $@"
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
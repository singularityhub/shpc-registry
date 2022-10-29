---
layout: container
name:  "quay.io/biocontainers/freyja"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/freyja/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/freyja/container.yaml"
updated_at: "2022-10-29 05:39:23.296194"
latest: "1.3.9--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/freyja"
aliases:
 - "faToVcf"
 - "fido2-assert"
 - "fido2-cred"
 - "fido2-token"
 - "freyja"
 - "ivar"
 - "matOptimize"
 - "matUtils"
 - "ripples"
 - "scp"
 - "sftp"
 - "ssh"
 - "ssh-add"
 - "ssh-agent"
 - "ssh-keygen"
 - "ssh-keyscan"
 - "sshd"
 - "usher"
 - "2to3-3.10"
 - "ace2sam"
 - "aggregate_profile.pl"
 - "bgzip"
 - "blast2sam.pl"
 - "bowtie2sam.pl"
 - "brotli"
 - "cwebp"
 - "dwebp"
 - "einsi"
versions:
 - "1.3.9--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for freyja"
config: {"url": "https://biocontainers.pro/tools/freyja", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for freyja", "latest": {"1.3.9--pyhdfd78af_0": "sha256:d5a2f3350b27d0fbe1fcf26567a92512545d3ef99d31f0c52a9ddb42a6f8c225"}, "tags": {"1.3.9--pyhdfd78af_0": "sha256:d5a2f3350b27d0fbe1fcf26567a92512545d3ef99d31f0c52a9ddb42a6f8c225"}, "docker": "quay.io/biocontainers/freyja", "aliases": {"faToVcf": "/usr/local/bin/faToVcf", "fido2-assert": "/usr/local/bin/fido2-assert", "fido2-cred": "/usr/local/bin/fido2-cred", "fido2-token": "/usr/local/bin/fido2-token", "freyja": "/usr/local/bin/freyja", "ivar": "/usr/local/bin/ivar", "matOptimize": "/usr/local/bin/matOptimize", "matUtils": "/usr/local/bin/matUtils", "ripples": "/usr/local/bin/ripples", "scp": "/usr/local/bin/scp", "sftp": "/usr/local/bin/sftp", "ssh": "/usr/local/bin/ssh", "ssh-add": "/usr/local/bin/ssh-add", "ssh-agent": "/usr/local/bin/ssh-agent", "ssh-keygen": "/usr/local/bin/ssh-keygen", "ssh-keyscan": "/usr/local/bin/ssh-keyscan", "sshd": "/usr/local/bin/sshd", "usher": "/usr/local/bin/usher", "2to3-3.10": "/usr/local/bin/2to3-3.10", "ace2sam": "/usr/local/bin/ace2sam", "aggregate_profile.pl": "/usr/local/bin/aggregate_profile.pl", "bgzip": "/usr/local/bin/bgzip", "blast2sam.pl": "/usr/local/bin/blast2sam.pl", "bowtie2sam.pl": "/usr/local/bin/bowtie2sam.pl", "brotli": "/usr/local/bin/brotli", "cwebp": "/usr/local/bin/cwebp", "dwebp": "/usr/local/bin/dwebp", "einsi": "/usr/local/bin/einsi"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/freyja.
shpc-registry automated BioContainers addition for freyja
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/freyja
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/freyja:1.3.9--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/freyja/1.3.9--pyhdfd78af_0
$ module help quay.io/biocontainers/freyja/1.3.9--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### freyja-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### freyja-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### freyja-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### freyja-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### freyja-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### freyja-inspect-deffile:

```bash
$ singularity inspect -d <container>
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


#### freyja

```bash
$ singularity exec <container> /usr/local/bin/freyja
$ podman run --it --rm --entrypoint /usr/local/bin/freyja   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/freyja   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ivar

```bash
$ singularity exec <container> /usr/local/bin/ivar
$ podman run --it --rm --entrypoint /usr/local/bin/ivar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ivar   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### ripples

```bash
$ singularity exec <container> /usr/local/bin/ripples
$ podman run --it --rm --entrypoint /usr/local/bin/ripples   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ripples   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### usher

```bash
$ singularity exec <container> /usr/local/bin/usher
$ podman run --it --rm --entrypoint /usr/local/bin/usher   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/usher   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace2sam

```bash
$ singularity exec <container> /usr/local/bin/ace2sam
$ podman run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aggregate_profile.pl

```bash
$ singularity exec <container> /usr/local/bin/aggregate_profile.pl
$ podman run --it --rm --entrypoint /usr/local/bin/aggregate_profile.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aggregate_profile.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/blast2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/bowtie2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### brotli

```bash
$ singularity exec <container> /usr/local/bin/brotli
$ podman run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cwebp

```bash
$ singularity exec <container> /usr/local/bin/cwebp
$ podman run --it --rm --entrypoint /usr/local/bin/cwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dwebp

```bash
$ singularity exec <container> /usr/local/bin/dwebp
$ podman run --it --rm --entrypoint /usr/local/bin/dwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### einsi

```bash
$ singularity exec <container> /usr/local/bin/einsi
$ podman run --it --rm --entrypoint /usr/local/bin/einsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/einsi   -v ${PWD} -w ${PWD} <container> -c " $@"
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
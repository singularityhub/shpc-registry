---
layout: container
name:  "quay.io/biocontainers/moff"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/moff/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/moff/container.yaml"
updated_at: "2023-07-28 03:33:26.612019"
latest: "2.0.3--hdfd78af_5"
container_url: "https://biocontainers.pro/tools/moff"
aliases:
 - "aprofutil"
 - "csc"
 - "csi"
 - "illinkanalyzer"
 - "moff_all.py"
 - "mono-hang-watchdog"
 - "vbc"
 - "mono-package-runtime"
 - "sgen-grep-binprot"
 - "al"
 - "al2"
 - "caspol"
 - "cccheck"
 - "ccrewrite"
 - "cert-sync"
 - "cert2spc"
 - "certmgr"
versions:
 - "2.0.3--hdfd78af_5"
description: "shpc-registry automated BioContainers addition for moff"
config: {"url": "https://biocontainers.pro/tools/moff", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for moff", "latest": {"2.0.3--hdfd78af_5": "sha256:39d5c82e3f32c6fb9519b012301787f30382e2701b1ae9c900dad01f2c96fee6"}, "tags": {"2.0.3--hdfd78af_5": "sha256:39d5c82e3f32c6fb9519b012301787f30382e2701b1ae9c900dad01f2c96fee6"}, "docker": "quay.io/biocontainers/moff", "aliases": {"aprofutil": "/usr/local/bin/aprofutil", "csc": "/usr/local/bin/csc", "csi": "/usr/local/bin/csi", "illinkanalyzer": "/usr/local/bin/illinkanalyzer", "moff_all.py": "/usr/local/bin/moff_all.py", "mono-hang-watchdog": "/usr/local/bin/mono-hang-watchdog", "vbc": "/usr/local/bin/vbc", "mono-package-runtime": "/usr/local/bin/mono-package-runtime", "sgen-grep-binprot": "/usr/local/bin/sgen-grep-binprot", "al": "/usr/local/bin/al", "al2": "/usr/local/bin/al2", "caspol": "/usr/local/bin/caspol", "cccheck": "/usr/local/bin/cccheck", "ccrewrite": "/usr/local/bin/ccrewrite", "cert-sync": "/usr/local/bin/cert-sync", "cert2spc": "/usr/local/bin/cert2spc", "certmgr": "/usr/local/bin/certmgr"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/moff.
shpc-registry automated BioContainers addition for moff
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/moff
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/moff:2.0.3--hdfd78af_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/moff/2.0.3--hdfd78af_5
$ module help quay.io/biocontainers/moff/2.0.3--hdfd78af_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### moff-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### moff-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### moff-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### moff-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### moff-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### moff-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### aprofutil

```bash
$ singularity exec <container> /usr/local/bin/aprofutil
$ podman run --it --rm --entrypoint /usr/local/bin/aprofutil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aprofutil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csc

```bash
$ singularity exec <container> /usr/local/bin/csc
$ podman run --it --rm --entrypoint /usr/local/bin/csc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csi

```bash
$ singularity exec <container> /usr/local/bin/csi
$ podman run --it --rm --entrypoint /usr/local/bin/csi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### illinkanalyzer

```bash
$ singularity exec <container> /usr/local/bin/illinkanalyzer
$ podman run --it --rm --entrypoint /usr/local/bin/illinkanalyzer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/illinkanalyzer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### moff_all.py

```bash
$ singularity exec <container> /usr/local/bin/moff_all.py
$ podman run --it --rm --entrypoint /usr/local/bin/moff_all.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/moff_all.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mono-hang-watchdog

```bash
$ singularity exec <container> /usr/local/bin/mono-hang-watchdog
$ podman run --it --rm --entrypoint /usr/local/bin/mono-hang-watchdog   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mono-hang-watchdog   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vbc

```bash
$ singularity exec <container> /usr/local/bin/vbc
$ podman run --it --rm --entrypoint /usr/local/bin/vbc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vbc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mono-package-runtime

```bash
$ singularity exec <container> /usr/local/bin/mono-package-runtime
$ podman run --it --rm --entrypoint /usr/local/bin/mono-package-runtime   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mono-package-runtime   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sgen-grep-binprot

```bash
$ singularity exec <container> /usr/local/bin/sgen-grep-binprot
$ podman run --it --rm --entrypoint /usr/local/bin/sgen-grep-binprot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sgen-grep-binprot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### al

```bash
$ singularity exec <container> /usr/local/bin/al
$ podman run --it --rm --entrypoint /usr/local/bin/al   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/al   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### al2

```bash
$ singularity exec <container> /usr/local/bin/al2
$ podman run --it --rm --entrypoint /usr/local/bin/al2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/al2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### caspol

```bash
$ singularity exec <container> /usr/local/bin/caspol
$ podman run --it --rm --entrypoint /usr/local/bin/caspol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/caspol   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cccheck

```bash
$ singularity exec <container> /usr/local/bin/cccheck
$ podman run --it --rm --entrypoint /usr/local/bin/cccheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cccheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ccrewrite

```bash
$ singularity exec <container> /usr/local/bin/ccrewrite
$ podman run --it --rm --entrypoint /usr/local/bin/ccrewrite   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ccrewrite   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cert-sync

```bash
$ singularity exec <container> /usr/local/bin/cert-sync
$ podman run --it --rm --entrypoint /usr/local/bin/cert-sync   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cert-sync   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cert2spc

```bash
$ singularity exec <container> /usr/local/bin/cert2spc
$ podman run --it --rm --entrypoint /usr/local/bin/cert2spc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cert2spc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### certmgr

```bash
$ singularity exec <container> /usr/local/bin/certmgr
$ podman run --it --rm --entrypoint /usr/local/bin/certmgr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/certmgr   -v ${PWD} -w ${PWD} <container> -c " $@"
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
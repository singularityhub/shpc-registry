---
layout: container
name:  "quay.io/biocontainers/searchgui"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/searchgui/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/searchgui/container.yaml"
updated_at: "2023-03-20 03:20:02.341789"
latest: "3.3.10--h470a237_0"
container_url: "https://biocontainers.pro/tools/searchgui"
aliases:
 - "csc"
 - "csc-dim"
 - "csi"
 - "illinkanalyzer"
 - "monograph"
 - "nunit-console"
 - "nunit-console2"
 - "nunit-console4"
 - "searchgui"
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
 - "3.3.9--1"
 - "3.3.10--h470a237_0"
description: "shpc-registry automated BioContainers addition for searchgui"
config: {"url": "https://biocontainers.pro/tools/searchgui", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for searchgui", "latest": {"3.3.10--h470a237_0": "sha256:4da9144fdc9d12215e928886934c02c4a15a4342f131bc8607fd4357ddd1eb8a"}, "tags": {"3.3.9--1": "sha256:aa164bf07a166fcc397a07cd5d9b51df9162a3253ea9ab0bbabcac420a3cdbce", "3.3.10--h470a237_0": "sha256:4da9144fdc9d12215e928886934c02c4a15a4342f131bc8607fd4357ddd1eb8a"}, "docker": "quay.io/biocontainers/searchgui", "aliases": {"csc": "/usr/local/bin/csc", "csc-dim": "/usr/local/bin/csc-dim", "csi": "/usr/local/bin/csi", "illinkanalyzer": "/usr/local/bin/illinkanalyzer", "monograph": "/usr/local/bin/monograph", "nunit-console": "/usr/local/bin/nunit-console", "nunit-console2": "/usr/local/bin/nunit-console2", "nunit-console4": "/usr/local/bin/nunit-console4", "searchgui": "/usr/local/bin/searchgui", "vbc": "/usr/local/bin/vbc", "mono-package-runtime": "/usr/local/bin/mono-package-runtime", "sgen-grep-binprot": "/usr/local/bin/sgen-grep-binprot", "al": "/usr/local/bin/al", "al2": "/usr/local/bin/al2", "caspol": "/usr/local/bin/caspol", "cccheck": "/usr/local/bin/cccheck", "ccrewrite": "/usr/local/bin/ccrewrite", "cert-sync": "/usr/local/bin/cert-sync", "cert2spc": "/usr/local/bin/cert2spc", "certmgr": "/usr/local/bin/certmgr"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/searchgui.
shpc-registry automated BioContainers addition for searchgui
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/searchgui
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/searchgui:3.3.10--h470a237_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/searchgui/3.3.10--h470a237_0
$ module help quay.io/biocontainers/searchgui/3.3.10--h470a237_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### searchgui-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### searchgui-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### searchgui-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### searchgui-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### searchgui-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### searchgui-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### csc

```bash
$ singularity exec <container> /usr/local/bin/csc
$ podman run --it --rm --entrypoint /usr/local/bin/csc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csc-dim

```bash
$ singularity exec <container> /usr/local/bin/csc-dim
$ podman run --it --rm --entrypoint /usr/local/bin/csc-dim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csc-dim   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### monograph

```bash
$ singularity exec <container> /usr/local/bin/monograph
$ podman run --it --rm --entrypoint /usr/local/bin/monograph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/monograph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nunit-console

```bash
$ singularity exec <container> /usr/local/bin/nunit-console
$ podman run --it --rm --entrypoint /usr/local/bin/nunit-console   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nunit-console   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nunit-console2

```bash
$ singularity exec <container> /usr/local/bin/nunit-console2
$ podman run --it --rm --entrypoint /usr/local/bin/nunit-console2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nunit-console2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nunit-console4

```bash
$ singularity exec <container> /usr/local/bin/nunit-console4
$ podman run --it --rm --entrypoint /usr/local/bin/nunit-console4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nunit-console4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### searchgui

```bash
$ singularity exec <container> /usr/local/bin/searchgui
$ podman run --it --rm --entrypoint /usr/local/bin/searchgui   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/searchgui   -v ${PWD} -w ${PWD} <container> -c " $@"
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
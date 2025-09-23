---
layout: container
name:  "quay.io/biocontainers/esme_psmpi_5_12_1"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/esme_psmpi_5_12_1/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/esme_psmpi_5_12_1/container.yaml"
updated_at: "2025-09-23 03:20:04.485535"
latest: "1.0.2--psmpi__h90a7f1b_0"
container_url: "https://biocontainers.pro/tools/esme_psmpi_5_12_1"
aliases:
 - "fido2-assert"
 - "fido2-cred"
 - "fido2-token"
 - "pcc"
 - "prte-info"
 - "prte-submit"
 - "prte-term"
 - "scp"
 - "sftp"
 - "ssh"
 - "ssh-add"
 - "ssh-agent"
 - "ssh-keygen"
 - "ssh-keyscan"
 - "sshd"
 - "prte"
 - "prte_info"
 - "prted"
 - "prterun"
 - "pterm"
 - "prun"
 - "ESMF_PrintInfo"
 - "ESMF_PrintInfoC"
 - "ESMF_Regrid"
 - "ESMF_RegridWeightGen"
 - "ESMF_Scrip2Unstruct"
 - "ESMF_WebServController"
 - "ESMX_Builder"
 - "gost12-256-hash"
 - "gost12-512-hash"
 - "edonr256-hash"
 - "edonr512-hash"
 - "ccmake"
 - "cmake"
 - "cpack"
 - "ctest"
 - "ed2k-link"
 - "has160-hash"
 - "magnet-link"
 - "rhash"
versions:
 - "1.0.2--psmpi__h90a7f1b_0"
description: "singularity registry hpc automated addition for esme_psmpi_5_12_1"
config: {"url": "https://biocontainers.pro/tools/esme_psmpi_5_12_1", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for esme_psmpi_5_12_1", "latest": {"1.0.2--psmpi__h90a7f1b_0": "sha256:031dda342773d5a9fb721dfa96d6cbb2e721c6fd5fc6e68ced32d7631b632a22"}, "tags": {"1.0.2--psmpi__h90a7f1b_0": "sha256:031dda342773d5a9fb721dfa96d6cbb2e721c6fd5fc6e68ced32d7631b632a22"}, "docker": "quay.io/biocontainers/esme_psmpi_5_12_1", "aliases": {"fido2-assert": "/usr/local/bin/fido2-assert", "fido2-cred": "/usr/local/bin/fido2-cred", "fido2-token": "/usr/local/bin/fido2-token", "pcc": "/usr/local/bin/pcc", "prte-info": "/usr/local/bin/prte-info", "prte-submit": "/usr/local/bin/prte-submit", "prte-term": "/usr/local/bin/prte-term", "scp": "/usr/local/bin/scp", "sftp": "/usr/local/bin/sftp", "ssh": "/usr/local/bin/ssh", "ssh-add": "/usr/local/bin/ssh-add", "ssh-agent": "/usr/local/bin/ssh-agent", "ssh-keygen": "/usr/local/bin/ssh-keygen", "ssh-keyscan": "/usr/local/bin/ssh-keyscan", "sshd": "/usr/local/bin/sshd", "prte": "/usr/local/bin/prte", "prte_info": "/usr/local/bin/prte_info", "prted": "/usr/local/bin/prted", "prterun": "/usr/local/bin/prterun", "pterm": "/usr/local/bin/pterm", "prun": "/usr/local/bin/prun", "ESMF_PrintInfo": "/usr/local/bin/ESMF_PrintInfo", "ESMF_PrintInfoC": "/usr/local/bin/ESMF_PrintInfoC", "ESMF_Regrid": "/usr/local/bin/ESMF_Regrid", "ESMF_RegridWeightGen": "/usr/local/bin/ESMF_RegridWeightGen", "ESMF_Scrip2Unstruct": "/usr/local/bin/ESMF_Scrip2Unstruct", "ESMF_WebServController": "/usr/local/bin/ESMF_WebServController", "ESMX_Builder": "/usr/local/bin/ESMX_Builder", "gost12-256-hash": "/usr/local/bin/gost12-256-hash", "gost12-512-hash": "/usr/local/bin/gost12-512-hash", "edonr256-hash": "/usr/local/bin/edonr256-hash", "edonr512-hash": "/usr/local/bin/edonr512-hash", "ccmake": "/usr/local/bin/ccmake", "cmake": "/usr/local/bin/cmake", "cpack": "/usr/local/bin/cpack", "ctest": "/usr/local/bin/ctest", "ed2k-link": "/usr/local/bin/ed2k-link", "has160-hash": "/usr/local/bin/has160-hash", "magnet-link": "/usr/local/bin/magnet-link", "rhash": "/usr/local/bin/rhash"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/esme_psmpi_5_12_1.
singularity registry hpc automated addition for esme_psmpi_5_12_1
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/esme_psmpi_5_12_1
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/esme_psmpi_5_12_1:1.0.2--psmpi__h90a7f1b_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/esme_psmpi_5_12_1/1.0.2--psmpi__h90a7f1b_0
$ module help quay.io/biocontainers/esme_psmpi_5_12_1/1.0.2--psmpi__h90a7f1b_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### esme_psmpi_5_12_1-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### esme_psmpi_5_12_1-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### esme_psmpi_5_12_1-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### esme_psmpi_5_12_1-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### esme_psmpi_5_12_1-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### esme_psmpi_5_12_1-inspect-deffile:

```bash
$ singularity inspect -d <container>
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


#### pcc

```bash
$ singularity exec <container> /usr/local/bin/pcc
$ podman run --it --rm --entrypoint /usr/local/bin/pcc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pcc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prte-info

```bash
$ singularity exec <container> /usr/local/bin/prte-info
$ podman run --it --rm --entrypoint /usr/local/bin/prte-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prte-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prte-submit

```bash
$ singularity exec <container> /usr/local/bin/prte-submit
$ podman run --it --rm --entrypoint /usr/local/bin/prte-submit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prte-submit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prte-term

```bash
$ singularity exec <container> /usr/local/bin/prte-term
$ podman run --it --rm --entrypoint /usr/local/bin/prte-term   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prte-term   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### prte

```bash
$ singularity exec <container> /usr/local/bin/prte
$ podman run --it --rm --entrypoint /usr/local/bin/prte   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prte   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prte_info

```bash
$ singularity exec <container> /usr/local/bin/prte_info
$ podman run --it --rm --entrypoint /usr/local/bin/prte_info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prte_info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prted

```bash
$ singularity exec <container> /usr/local/bin/prted
$ podman run --it --rm --entrypoint /usr/local/bin/prted   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prted   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prterun

```bash
$ singularity exec <container> /usr/local/bin/prterun
$ podman run --it --rm --entrypoint /usr/local/bin/prterun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prterun   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pterm

```bash
$ singularity exec <container> /usr/local/bin/pterm
$ podman run --it --rm --entrypoint /usr/local/bin/pterm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pterm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prun

```bash
$ singularity exec <container> /usr/local/bin/prun
$ podman run --it --rm --entrypoint /usr/local/bin/prun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prun   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ESMF_PrintInfo

```bash
$ singularity exec <container> /usr/local/bin/ESMF_PrintInfo
$ podman run --it --rm --entrypoint /usr/local/bin/ESMF_PrintInfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ESMF_PrintInfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ESMF_PrintInfoC

```bash
$ singularity exec <container> /usr/local/bin/ESMF_PrintInfoC
$ podman run --it --rm --entrypoint /usr/local/bin/ESMF_PrintInfoC   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ESMF_PrintInfoC   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ESMF_Regrid

```bash
$ singularity exec <container> /usr/local/bin/ESMF_Regrid
$ podman run --it --rm --entrypoint /usr/local/bin/ESMF_Regrid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ESMF_Regrid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ESMF_RegridWeightGen

```bash
$ singularity exec <container> /usr/local/bin/ESMF_RegridWeightGen
$ podman run --it --rm --entrypoint /usr/local/bin/ESMF_RegridWeightGen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ESMF_RegridWeightGen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ESMF_Scrip2Unstruct

```bash
$ singularity exec <container> /usr/local/bin/ESMF_Scrip2Unstruct
$ podman run --it --rm --entrypoint /usr/local/bin/ESMF_Scrip2Unstruct   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ESMF_Scrip2Unstruct   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ESMF_WebServController

```bash
$ singularity exec <container> /usr/local/bin/ESMF_WebServController
$ podman run --it --rm --entrypoint /usr/local/bin/ESMF_WebServController   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ESMF_WebServController   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ESMX_Builder

```bash
$ singularity exec <container> /usr/local/bin/ESMX_Builder
$ podman run --it --rm --entrypoint /usr/local/bin/ESMX_Builder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ESMX_Builder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gost12-256-hash

```bash
$ singularity exec <container> /usr/local/bin/gost12-256-hash
$ podman run --it --rm --entrypoint /usr/local/bin/gost12-256-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gost12-256-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gost12-512-hash

```bash
$ singularity exec <container> /usr/local/bin/gost12-512-hash
$ podman run --it --rm --entrypoint /usr/local/bin/gost12-512-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gost12-512-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### edonr256-hash

```bash
$ singularity exec <container> /usr/local/bin/edonr256-hash
$ podman run --it --rm --entrypoint /usr/local/bin/edonr256-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/edonr256-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### edonr512-hash

```bash
$ singularity exec <container> /usr/local/bin/edonr512-hash
$ podman run --it --rm --entrypoint /usr/local/bin/edonr512-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/edonr512-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ccmake

```bash
$ singularity exec <container> /usr/local/bin/ccmake
$ podman run --it --rm --entrypoint /usr/local/bin/ccmake   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ccmake   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmake

```bash
$ singularity exec <container> /usr/local/bin/cmake
$ podman run --it --rm --entrypoint /usr/local/bin/cmake   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmake   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cpack

```bash
$ singularity exec <container> /usr/local/bin/cpack
$ podman run --it --rm --entrypoint /usr/local/bin/cpack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cpack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ctest

```bash
$ singularity exec <container> /usr/local/bin/ctest
$ podman run --it --rm --entrypoint /usr/local/bin/ctest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ctest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ed2k-link

```bash
$ singularity exec <container> /usr/local/bin/ed2k-link
$ podman run --it --rm --entrypoint /usr/local/bin/ed2k-link   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ed2k-link   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### has160-hash

```bash
$ singularity exec <container> /usr/local/bin/has160-hash
$ podman run --it --rm --entrypoint /usr/local/bin/has160-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/has160-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### magnet-link

```bash
$ singularity exec <container> /usr/local/bin/magnet-link
$ podman run --it --rm --entrypoint /usr/local/bin/magnet-link   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/magnet-link   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rhash

```bash
$ singularity exec <container> /usr/local/bin/rhash
$ podman run --it --rm --entrypoint /usr/local/bin/rhash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rhash   -v ${PWD} -w ${PWD} <container> -c " $@"
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
---
layout: container
name:  "quay.io/biocontainers/esme_esmf_psmpi_5_12_1"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/esme_esmf_psmpi_5_12_1/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/esme_esmf_psmpi_5_12_1/container.yaml"
updated_at: "2025-09-13 02:53:35.650718"
latest: "8.9.0--h499a0f0_0"
container_url: "https://biocontainers.pro/tools/esme_esmf_psmpi_5_12_1"
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
 - "nc4print"
 - "ocprint"
 - "chacl"
 - "getfacl"
 - "setfacl"
 - "cdfdiff"
 - "ncmpidiff"
 - "ncmpidump"
 - "ncmpigen"
 - "ncoffsets"
 - "ncvalidator"
 - "pnetcdf-config"
versions:
 - "8.9.0--h499a0f0_0"
description: "singularity registry hpc automated addition for esme_esmf_psmpi_5_12_1"
config: {"url": "https://biocontainers.pro/tools/esme_esmf_psmpi_5_12_1", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for esme_esmf_psmpi_5_12_1", "latest": {"8.9.0--h499a0f0_0": "sha256:f5e38d4db531abbbecbef41326ac2e702c06f19297644423d496a1c3ef4177dc"}, "tags": {"8.9.0--h499a0f0_0": "sha256:f5e38d4db531abbbecbef41326ac2e702c06f19297644423d496a1c3ef4177dc"}, "docker": "quay.io/biocontainers/esme_esmf_psmpi_5_12_1", "aliases": {"fido2-assert": "/usr/local/bin/fido2-assert", "fido2-cred": "/usr/local/bin/fido2-cred", "fido2-token": "/usr/local/bin/fido2-token", "pcc": "/usr/local/bin/pcc", "prte-info": "/usr/local/bin/prte-info", "prte-submit": "/usr/local/bin/prte-submit", "prte-term": "/usr/local/bin/prte-term", "scp": "/usr/local/bin/scp", "sftp": "/usr/local/bin/sftp", "ssh": "/usr/local/bin/ssh", "ssh-add": "/usr/local/bin/ssh-add", "ssh-agent": "/usr/local/bin/ssh-agent", "ssh-keygen": "/usr/local/bin/ssh-keygen", "ssh-keyscan": "/usr/local/bin/ssh-keyscan", "sshd": "/usr/local/bin/sshd", "prte": "/usr/local/bin/prte", "prte_info": "/usr/local/bin/prte_info", "prted": "/usr/local/bin/prted", "prterun": "/usr/local/bin/prterun", "pterm": "/usr/local/bin/pterm", "prun": "/usr/local/bin/prun", "ESMF_PrintInfo": "/usr/local/bin/ESMF_PrintInfo", "ESMF_PrintInfoC": "/usr/local/bin/ESMF_PrintInfoC", "ESMF_Regrid": "/usr/local/bin/ESMF_Regrid", "ESMF_RegridWeightGen": "/usr/local/bin/ESMF_RegridWeightGen", "ESMF_Scrip2Unstruct": "/usr/local/bin/ESMF_Scrip2Unstruct", "ESMF_WebServController": "/usr/local/bin/ESMF_WebServController", "ESMX_Builder": "/usr/local/bin/ESMX_Builder", "nc4print": "/usr/local/bin/nc4print", "ocprint": "/usr/local/bin/ocprint", "chacl": "/usr/local/bin/chacl", "getfacl": "/usr/local/bin/getfacl", "setfacl": "/usr/local/bin/setfacl", "cdfdiff": "/usr/local/bin/cdfdiff", "ncmpidiff": "/usr/local/bin/ncmpidiff", "ncmpidump": "/usr/local/bin/ncmpidump", "ncmpigen": "/usr/local/bin/ncmpigen", "ncoffsets": "/usr/local/bin/ncoffsets", "ncvalidator": "/usr/local/bin/ncvalidator", "pnetcdf-config": "/usr/local/bin/pnetcdf-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/esme_esmf_psmpi_5_12_1.
singularity registry hpc automated addition for esme_esmf_psmpi_5_12_1
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/esme_esmf_psmpi_5_12_1
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/esme_esmf_psmpi_5_12_1:8.9.0--h499a0f0_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/esme_esmf_psmpi_5_12_1/8.9.0--h499a0f0_0
$ module help quay.io/biocontainers/esme_esmf_psmpi_5_12_1/8.9.0--h499a0f0_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### esme_esmf_psmpi_5_12_1-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### esme_esmf_psmpi_5_12_1-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### esme_esmf_psmpi_5_12_1-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### esme_esmf_psmpi_5_12_1-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### esme_esmf_psmpi_5_12_1-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### esme_esmf_psmpi_5_12_1-inspect-deffile:

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


#### nc4print

```bash
$ singularity exec <container> /usr/local/bin/nc4print
$ podman run --it --rm --entrypoint /usr/local/bin/nc4print   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nc4print   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ocprint

```bash
$ singularity exec <container> /usr/local/bin/ocprint
$ podman run --it --rm --entrypoint /usr/local/bin/ocprint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ocprint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chacl

```bash
$ singularity exec <container> /usr/local/bin/chacl
$ podman run --it --rm --entrypoint /usr/local/bin/chacl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chacl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getfacl

```bash
$ singularity exec <container> /usr/local/bin/getfacl
$ podman run --it --rm --entrypoint /usr/local/bin/getfacl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getfacl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### setfacl

```bash
$ singularity exec <container> /usr/local/bin/setfacl
$ podman run --it --rm --entrypoint /usr/local/bin/setfacl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/setfacl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cdfdiff

```bash
$ singularity exec <container> /usr/local/bin/cdfdiff
$ podman run --it --rm --entrypoint /usr/local/bin/cdfdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cdfdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncmpidiff

```bash
$ singularity exec <container> /usr/local/bin/ncmpidiff
$ podman run --it --rm --entrypoint /usr/local/bin/ncmpidiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncmpidiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncmpidump

```bash
$ singularity exec <container> /usr/local/bin/ncmpidump
$ podman run --it --rm --entrypoint /usr/local/bin/ncmpidump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncmpidump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncmpigen

```bash
$ singularity exec <container> /usr/local/bin/ncmpigen
$ podman run --it --rm --entrypoint /usr/local/bin/ncmpigen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncmpigen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncoffsets

```bash
$ singularity exec <container> /usr/local/bin/ncoffsets
$ podman run --it --rm --entrypoint /usr/local/bin/ncoffsets   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncoffsets   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncvalidator

```bash
$ singularity exec <container> /usr/local/bin/ncvalidator
$ podman run --it --rm --entrypoint /usr/local/bin/ncvalidator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncvalidator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pnetcdf-config

```bash
$ singularity exec <container> /usr/local/bin/pnetcdf-config
$ podman run --it --rm --entrypoint /usr/local/bin/pnetcdf-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pnetcdf-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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
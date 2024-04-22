---
layout: container
name:  "quay.io/biocontainers/disco"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/disco/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/disco/container.yaml"
updated_at: "2024-04-22 03:09:38.733210"
latest: "1.2--h43eeafb_6"
container_url: "https://biocontainers.pro/tools/disco"
aliases:
 - "buildG"
 - "buildG-MPI"
 - "buildG-MPIRMA"
 - "disco.cfg"
 - "disco_2.cfg"
 - "disco_3.cfg"
 - "fido2-assert"
 - "fido2-cred"
 - "fido2-token"
 - "fullsimplify"
 - "parsimplify"
 - "runAssembly-MPI.sh"
 - "runAssembly.sh"
 - "runDisco-MPI-ALPS.sh"
 - "runDisco-MPI-AllineaMAP.sh"
 - "runDisco-MPI-SLURM.sh"
 - "runDisco-MPI.sh"
 - "runDisco.sh"
 - "runECC.sh"
 - "scp"
 - "sftp"
 - "ssh"
 - "ssh-add"
 - "ssh-agent"
 - "ssh-keygen"
 - "ssh-keyscan"
 - "sshd"
 - "kmutate.sh"
 - "runhmm.sh"
 - "kmerposition.sh"
 - "reformatpb.sh"
 - "summarizecoverage.sh"
 - "alltoall.sh"
 - "analyzesketchresults.sh"
 - "comparessu.sh"
 - "filtersilva.sh"
 - "sketchblacklist2.sh"
versions:
 - "1.2--h5b5514e_5"
 - "1.2--h43eeafb_6"
description: "shpc-registry automated BioContainers addition for disco"
config: {"url": "https://biocontainers.pro/tools/disco", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for disco", "latest": {"1.2--h43eeafb_6": "sha256:dd6db5c54bf38ae0555dbb967a3420250b50ac894494956bd95e30a595d323a0"}, "tags": {"1.2--h5b5514e_5": "sha256:141ebbe6888731e5cb93b7b10a8835d210323db21ead0b4364c1e204eac457f5", "1.2--h43eeafb_6": "sha256:dd6db5c54bf38ae0555dbb967a3420250b50ac894494956bd95e30a595d323a0"}, "docker": "quay.io/biocontainers/disco", "aliases": {"buildG": "/usr/local/bin/buildG", "buildG-MPI": "/usr/local/bin/buildG-MPI", "buildG-MPIRMA": "/usr/local/bin/buildG-MPIRMA", "disco.cfg": "/usr/local/bin/disco.cfg", "disco_2.cfg": "/usr/local/bin/disco_2.cfg", "disco_3.cfg": "/usr/local/bin/disco_3.cfg", "fido2-assert": "/usr/local/bin/fido2-assert", "fido2-cred": "/usr/local/bin/fido2-cred", "fido2-token": "/usr/local/bin/fido2-token", "fullsimplify": "/usr/local/bin/fullsimplify", "parsimplify": "/usr/local/bin/parsimplify", "runAssembly-MPI.sh": "/usr/local/bin/runAssembly-MPI.sh", "runAssembly.sh": "/usr/local/bin/runAssembly.sh", "runDisco-MPI-ALPS.sh": "/usr/local/bin/runDisco-MPI-ALPS.sh", "runDisco-MPI-AllineaMAP.sh": "/usr/local/bin/runDisco-MPI-AllineaMAP.sh", "runDisco-MPI-SLURM.sh": "/usr/local/bin/runDisco-MPI-SLURM.sh", "runDisco-MPI.sh": "/usr/local/bin/runDisco-MPI.sh", "runDisco.sh": "/usr/local/bin/runDisco.sh", "runECC.sh": "/usr/local/bin/runECC.sh", "scp": "/usr/local/bin/scp", "sftp": "/usr/local/bin/sftp", "ssh": "/usr/local/bin/ssh", "ssh-add": "/usr/local/bin/ssh-add", "ssh-agent": "/usr/local/bin/ssh-agent", "ssh-keygen": "/usr/local/bin/ssh-keygen", "ssh-keyscan": "/usr/local/bin/ssh-keyscan", "sshd": "/usr/local/bin/sshd", "kmutate.sh": "/usr/local/bin/kmutate.sh", "runhmm.sh": "/usr/local/bin/runhmm.sh", "kmerposition.sh": "/usr/local/bin/kmerposition.sh", "reformatpb.sh": "/usr/local/bin/reformatpb.sh", "summarizecoverage.sh": "/usr/local/bin/summarizecoverage.sh", "alltoall.sh": "/usr/local/bin/alltoall.sh", "analyzesketchresults.sh": "/usr/local/bin/analyzesketchresults.sh", "comparessu.sh": "/usr/local/bin/comparessu.sh", "filtersilva.sh": "/usr/local/bin/filtersilva.sh", "sketchblacklist2.sh": "/usr/local/bin/sketchblacklist2.sh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/disco.
shpc-registry automated BioContainers addition for disco
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/disco
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/disco:1.2--h43eeafb_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/disco/1.2--h43eeafb_6
$ module help quay.io/biocontainers/disco/1.2--h43eeafb_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### disco-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### disco-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### disco-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### disco-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### disco-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### disco-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### buildG

```bash
$ singularity exec <container> /usr/local/bin/buildG
$ podman run --it --rm --entrypoint /usr/local/bin/buildG   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/buildG   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### buildG-MPI

```bash
$ singularity exec <container> /usr/local/bin/buildG-MPI
$ podman run --it --rm --entrypoint /usr/local/bin/buildG-MPI   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/buildG-MPI   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### buildG-MPIRMA

```bash
$ singularity exec <container> /usr/local/bin/buildG-MPIRMA
$ podman run --it --rm --entrypoint /usr/local/bin/buildG-MPIRMA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/buildG-MPIRMA   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### disco.cfg

```bash
$ singularity exec <container> /usr/local/bin/disco.cfg
$ podman run --it --rm --entrypoint /usr/local/bin/disco.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/disco.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### disco_2.cfg

```bash
$ singularity exec <container> /usr/local/bin/disco_2.cfg
$ podman run --it --rm --entrypoint /usr/local/bin/disco_2.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/disco_2.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### disco_3.cfg

```bash
$ singularity exec <container> /usr/local/bin/disco_3.cfg
$ podman run --it --rm --entrypoint /usr/local/bin/disco_3.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/disco_3.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### fullsimplify

```bash
$ singularity exec <container> /usr/local/bin/fullsimplify
$ podman run --it --rm --entrypoint /usr/local/bin/fullsimplify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fullsimplify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parsimplify

```bash
$ singularity exec <container> /usr/local/bin/parsimplify
$ podman run --it --rm --entrypoint /usr/local/bin/parsimplify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parsimplify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runAssembly-MPI.sh

```bash
$ singularity exec <container> /usr/local/bin/runAssembly-MPI.sh
$ podman run --it --rm --entrypoint /usr/local/bin/runAssembly-MPI.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runAssembly-MPI.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runAssembly.sh

```bash
$ singularity exec <container> /usr/local/bin/runAssembly.sh
$ podman run --it --rm --entrypoint /usr/local/bin/runAssembly.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runAssembly.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runDisco-MPI-ALPS.sh

```bash
$ singularity exec <container> /usr/local/bin/runDisco-MPI-ALPS.sh
$ podman run --it --rm --entrypoint /usr/local/bin/runDisco-MPI-ALPS.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runDisco-MPI-ALPS.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runDisco-MPI-AllineaMAP.sh

```bash
$ singularity exec <container> /usr/local/bin/runDisco-MPI-AllineaMAP.sh
$ podman run --it --rm --entrypoint /usr/local/bin/runDisco-MPI-AllineaMAP.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runDisco-MPI-AllineaMAP.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runDisco-MPI-SLURM.sh

```bash
$ singularity exec <container> /usr/local/bin/runDisco-MPI-SLURM.sh
$ podman run --it --rm --entrypoint /usr/local/bin/runDisco-MPI-SLURM.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runDisco-MPI-SLURM.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runDisco-MPI.sh

```bash
$ singularity exec <container> /usr/local/bin/runDisco-MPI.sh
$ podman run --it --rm --entrypoint /usr/local/bin/runDisco-MPI.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runDisco-MPI.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runDisco.sh

```bash
$ singularity exec <container> /usr/local/bin/runDisco.sh
$ podman run --it --rm --entrypoint /usr/local/bin/runDisco.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runDisco.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runECC.sh

```bash
$ singularity exec <container> /usr/local/bin/runECC.sh
$ podman run --it --rm --entrypoint /usr/local/bin/runECC.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runECC.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### kmutate.sh

```bash
$ singularity exec <container> /usr/local/bin/kmutate.sh
$ podman run --it --rm --entrypoint /usr/local/bin/kmutate.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmutate.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runhmm.sh

```bash
$ singularity exec <container> /usr/local/bin/runhmm.sh
$ podman run --it --rm --entrypoint /usr/local/bin/runhmm.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runhmm.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmerposition.sh

```bash
$ singularity exec <container> /usr/local/bin/kmerposition.sh
$ podman run --it --rm --entrypoint /usr/local/bin/kmerposition.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmerposition.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### reformatpb.sh

```bash
$ singularity exec <container> /usr/local/bin/reformatpb.sh
$ podman run --it --rm --entrypoint /usr/local/bin/reformatpb.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/reformatpb.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### summarizecoverage.sh

```bash
$ singularity exec <container> /usr/local/bin/summarizecoverage.sh
$ podman run --it --rm --entrypoint /usr/local/bin/summarizecoverage.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/summarizecoverage.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alltoall.sh

```bash
$ singularity exec <container> /usr/local/bin/alltoall.sh
$ podman run --it --rm --entrypoint /usr/local/bin/alltoall.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alltoall.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### analyzesketchresults.sh

```bash
$ singularity exec <container> /usr/local/bin/analyzesketchresults.sh
$ podman run --it --rm --entrypoint /usr/local/bin/analyzesketchresults.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/analyzesketchresults.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### comparessu.sh

```bash
$ singularity exec <container> /usr/local/bin/comparessu.sh
$ podman run --it --rm --entrypoint /usr/local/bin/comparessu.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/comparessu.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filtersilva.sh

```bash
$ singularity exec <container> /usr/local/bin/filtersilva.sh
$ podman run --it --rm --entrypoint /usr/local/bin/filtersilva.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filtersilva.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sketchblacklist2.sh

```bash
$ singularity exec <container> /usr/local/bin/sketchblacklist2.sh
$ podman run --it --rm --entrypoint /usr/local/bin/sketchblacklist2.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sketchblacklist2.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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
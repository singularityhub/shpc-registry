---
layout: container
name:  "quay.io/biocontainers/fragpipe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fragpipe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fragpipe/container.yaml"
updated_at: "2025-09-10 03:14:13.636487"
latest: "23.1--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/fragpipe"
aliases:
 - "csc-dim"
 - "fragpipe"
 - "ionquant"
 - "monograph"
 - "msfragger"
 - "nunit-console"
 - "nunit-console2"
 - "nunit-console4"
 - "philosopher"
 - "csc"
 - "csi"
 - "illinkanalyzer"
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
 - "chktrust"
 - "crlupdate"
 - "csharp"
 - "dmcs"
 - "dtd2rng"
 - "dtd2xsd"
 - "gacutil"
 - "gacutil2"
 - "genxs"
 - "httpcfg"
 - "ikdasm"
versions:
 - "20.0--hdfd78af_0"
 - "20.0--hdfd78af_2"
 - "20.0--hdfd78af_3"
 - "20.0--hdfd78af_4"
 - "22.0--hdfd78af_0"
 - "23.0--hdfd78af_0"
 - "23.1--hdfd78af_0"
description: "singularity registry hpc automated addition for fragpipe"
config: {"url": "https://biocontainers.pro/tools/fragpipe", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for fragpipe", "latest": {"23.1--hdfd78af_0": "sha256:c75997a3b35087249bc01517b0e6d71d0ad8a8bc5952330f64ef0068020bc580"}, "tags": {"20.0--hdfd78af_0": "sha256:bd821a40d7cea6a4d9e098c5bcdb99cb34658ad223a98216841dbc3eede418a4", "20.0--hdfd78af_2": "sha256:6a4592367bd83d410a53b0a6a744864b76375893ff1af23c5a47ba427e0e3eff", "20.0--hdfd78af_3": "sha256:22d4c6e006136c073b8914ff99149bdd14d49c5198278a3ba6915e5c1dba7798", "20.0--hdfd78af_4": "sha256:e5bfaff4260912092ac83f63618de1f07fe7b3dc8add1c05bd363927c391ccb5", "22.0--hdfd78af_0": "sha256:a8361803a91a1194d4301a090dc940391ff303a1e07ec689771c5a37d512306d", "23.0--hdfd78af_0": "sha256:98e21a65da977c7b313a3fdc1f209eda19340b2331dd344a4b8d0f1de7914656", "23.1--hdfd78af_0": "sha256:c75997a3b35087249bc01517b0e6d71d0ad8a8bc5952330f64ef0068020bc580"}, "docker": "quay.io/biocontainers/fragpipe", "aliases": {"csc-dim": "/usr/local/bin/csc-dim", "fragpipe": "/usr/local/bin/fragpipe", "ionquant": "/usr/local/bin/ionquant", "monograph": "/usr/local/bin/monograph", "msfragger": "/usr/local/bin/msfragger", "nunit-console": "/usr/local/bin/nunit-console", "nunit-console2": "/usr/local/bin/nunit-console2", "nunit-console4": "/usr/local/bin/nunit-console4", "philosopher": "/usr/local/bin/philosopher", "csc": "/usr/local/bin/csc", "csi": "/usr/local/bin/csi", "illinkanalyzer": "/usr/local/bin/illinkanalyzer", "vbc": "/usr/local/bin/vbc", "mono-package-runtime": "/usr/local/bin/mono-package-runtime", "sgen-grep-binprot": "/usr/local/bin/sgen-grep-binprot", "al": "/usr/local/bin/al", "al2": "/usr/local/bin/al2", "caspol": "/usr/local/bin/caspol", "cccheck": "/usr/local/bin/cccheck", "ccrewrite": "/usr/local/bin/ccrewrite", "cert-sync": "/usr/local/bin/cert-sync", "cert2spc": "/usr/local/bin/cert2spc", "certmgr": "/usr/local/bin/certmgr", "chktrust": "/usr/local/bin/chktrust", "crlupdate": "/usr/local/bin/crlupdate", "csharp": "/usr/local/bin/csharp", "dmcs": "/usr/local/bin/dmcs", "dtd2rng": "/usr/local/bin/dtd2rng", "dtd2xsd": "/usr/local/bin/dtd2xsd", "gacutil": "/usr/local/bin/gacutil", "gacutil2": "/usr/local/bin/gacutil2", "genxs": "/usr/local/bin/genxs", "httpcfg": "/usr/local/bin/httpcfg", "ikdasm": "/usr/local/bin/ikdasm"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fragpipe.
singularity registry hpc automated addition for fragpipe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fragpipe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fragpipe:23.1--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fragpipe/23.1--hdfd78af_0
$ module help quay.io/biocontainers/fragpipe/23.1--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fragpipe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fragpipe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fragpipe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fragpipe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fragpipe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fragpipe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### csc-dim

```bash
$ singularity exec <container> /usr/local/bin/csc-dim
$ podman run --it --rm --entrypoint /usr/local/bin/csc-dim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csc-dim   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fragpipe

```bash
$ singularity exec <container> /usr/local/bin/fragpipe
$ podman run --it --rm --entrypoint /usr/local/bin/fragpipe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fragpipe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ionquant

```bash
$ singularity exec <container> /usr/local/bin/ionquant
$ podman run --it --rm --entrypoint /usr/local/bin/ionquant   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ionquant   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### monograph

```bash
$ singularity exec <container> /usr/local/bin/monograph
$ podman run --it --rm --entrypoint /usr/local/bin/monograph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/monograph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### msfragger

```bash
$ singularity exec <container> /usr/local/bin/msfragger
$ podman run --it --rm --entrypoint /usr/local/bin/msfragger   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/msfragger   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### philosopher

```bash
$ singularity exec <container> /usr/local/bin/philosopher
$ podman run --it --rm --entrypoint /usr/local/bin/philosopher   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/philosopher   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### chktrust

```bash
$ singularity exec <container> /usr/local/bin/chktrust
$ podman run --it --rm --entrypoint /usr/local/bin/chktrust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chktrust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### crlupdate

```bash
$ singularity exec <container> /usr/local/bin/crlupdate
$ podman run --it --rm --entrypoint /usr/local/bin/crlupdate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/crlupdate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csharp

```bash
$ singularity exec <container> /usr/local/bin/csharp
$ podman run --it --rm --entrypoint /usr/local/bin/csharp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csharp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dmcs

```bash
$ singularity exec <container> /usr/local/bin/dmcs
$ podman run --it --rm --entrypoint /usr/local/bin/dmcs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dmcs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dtd2rng

```bash
$ singularity exec <container> /usr/local/bin/dtd2rng
$ podman run --it --rm --entrypoint /usr/local/bin/dtd2rng   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dtd2rng   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dtd2xsd

```bash
$ singularity exec <container> /usr/local/bin/dtd2xsd
$ podman run --it --rm --entrypoint /usr/local/bin/dtd2xsd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dtd2xsd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gacutil

```bash
$ singularity exec <container> /usr/local/bin/gacutil
$ podman run --it --rm --entrypoint /usr/local/bin/gacutil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gacutil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gacutil2

```bash
$ singularity exec <container> /usr/local/bin/gacutil2
$ podman run --it --rm --entrypoint /usr/local/bin/gacutil2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gacutil2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genxs

```bash
$ singularity exec <container> /usr/local/bin/genxs
$ podman run --it --rm --entrypoint /usr/local/bin/genxs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genxs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### httpcfg

```bash
$ singularity exec <container> /usr/local/bin/httpcfg
$ podman run --it --rm --entrypoint /usr/local/bin/httpcfg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/httpcfg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ikdasm

```bash
$ singularity exec <container> /usr/local/bin/ikdasm
$ podman run --it --rm --entrypoint /usr/local/bin/ikdasm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ikdasm   -v ${PWD} -w ${PWD} <container> -c " $@"
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
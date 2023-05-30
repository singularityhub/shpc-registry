---
layout: container
name:  "quay.io/biocontainers/clinvar-tsv"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/clinvar-tsv/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/clinvar-tsv/container.yaml"
updated_at: "2023-05-30 02:53:32.357434"
latest: "0.5.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/clinvar-tsv"
aliases:
 - "clinvar_tsv"
 - "plac_runner.py"
 - "yte"
 - "docutils"
 - "pulptest"
 - "cbc"
 - "clp"
 - "snakemake"
 - "snakemake-bash-completion"
 - "tabulate"
 - "jupyter-trust"
versions:
 - "0.4.1--pyhdfd78af_0"
 - "0.5.0--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for clinvar-tsv"
config: {"url": "https://biocontainers.pro/tools/clinvar-tsv", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for clinvar-tsv", "latest": {"0.5.0--pyhdfd78af_0": "sha256:6cd096722e0679cd4ad3ec772e98dcd89deb35c4938b29840aa1da11fc12fb1d"}, "tags": {"0.4.1--pyhdfd78af_0": "sha256:34c80732e46c48667f40e081acb748630e47ff6d372d4fc17e6a82ea60d18295", "0.5.0--pyhdfd78af_0": "sha256:6cd096722e0679cd4ad3ec772e98dcd89deb35c4938b29840aa1da11fc12fb1d"}, "docker": "quay.io/biocontainers/clinvar-tsv", "aliases": {"clinvar_tsv": "/usr/local/bin/clinvar_tsv", "plac_runner.py": "/usr/local/bin/plac_runner.py", "yte": "/usr/local/bin/yte", "docutils": "/usr/local/bin/docutils", "pulptest": "/usr/local/bin/pulptest", "cbc": "/usr/local/bin/cbc", "clp": "/usr/local/bin/clp", "snakemake": "/usr/local/bin/snakemake", "snakemake-bash-completion": "/usr/local/bin/snakemake-bash-completion", "tabulate": "/usr/local/bin/tabulate", "jupyter-trust": "/usr/local/bin/jupyter-trust"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/clinvar-tsv.
shpc-registry automated BioContainers addition for clinvar-tsv
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/clinvar-tsv
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/clinvar-tsv:0.5.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/clinvar-tsv/0.5.0--pyhdfd78af_0
$ module help quay.io/biocontainers/clinvar-tsv/0.5.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### clinvar-tsv-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### clinvar-tsv-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### clinvar-tsv-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### clinvar-tsv-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### clinvar-tsv-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### clinvar-tsv-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### clinvar_tsv

```bash
$ singularity exec <container> /usr/local/bin/clinvar_tsv
$ podman run --it --rm --entrypoint /usr/local/bin/clinvar_tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clinvar_tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plac_runner.py

```bash
$ singularity exec <container> /usr/local/bin/plac_runner.py
$ podman run --it --rm --entrypoint /usr/local/bin/plac_runner.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plac_runner.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### yte

```bash
$ singularity exec <container> /usr/local/bin/yte
$ podman run --it --rm --entrypoint /usr/local/bin/yte   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yte   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### docutils

```bash
$ singularity exec <container> /usr/local/bin/docutils
$ podman run --it --rm --entrypoint /usr/local/bin/docutils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/docutils   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pulptest

```bash
$ singularity exec <container> /usr/local/bin/pulptest
$ podman run --it --rm --entrypoint /usr/local/bin/pulptest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pulptest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cbc

```bash
$ singularity exec <container> /usr/local/bin/cbc
$ podman run --it --rm --entrypoint /usr/local/bin/cbc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cbc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clp

```bash
$ singularity exec <container> /usr/local/bin/clp
$ podman run --it --rm --entrypoint /usr/local/bin/clp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snakemake

```bash
$ singularity exec <container> /usr/local/bin/snakemake
$ podman run --it --rm --entrypoint /usr/local/bin/snakemake   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snakemake   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snakemake-bash-completion

```bash
$ singularity exec <container> /usr/local/bin/snakemake-bash-completion
$ podman run --it --rm --entrypoint /usr/local/bin/snakemake-bash-completion   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snakemake-bash-completion   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabulate

```bash
$ singularity exec <container> /usr/local/bin/tabulate
$ podman run --it --rm --entrypoint /usr/local/bin/tabulate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabulate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-trust

```bash
$ singularity exec <container> /usr/local/bin/jupyter-trust
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-trust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-trust   -v ${PWD} -w ${PWD} <container> -c " $@"
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
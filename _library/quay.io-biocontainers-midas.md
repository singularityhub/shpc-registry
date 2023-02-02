---
layout: container
name:  "quay.io/biocontainers/midas"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/midas/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/midas/container.yaml"
updated_at: "2023-02-02 03:16:57.443968"
latest: "1.3.2--pyh7cba7a3_7"
container_url: "https://biocontainers.pro/tools/midas"
aliases:
 - "build_midas_db.py"
 - "call_consensus.py"
 - "compare_genes.py"
 - "hs-blastn"
 - "merge_midas.py"
 - "query_by_compound.py"
 - "run_midas.py"
 - "snp_diversity.py"
 - "strain_tracking.py"
 - "CA.pm"
 - "cacert.pem"
 - "index-themes"
 - "fetch-extras"
 - "go.mod"
 - "go.sum"
 - "hlp-xtract.txt"
 - "index-extras"
 - "pm-collect"
 - "readme.pdf"
versions:
 - "1.3.2--pyh5e36f6f_6"
 - "1.3.2--pyh7cba7a3_7"
description: "shpc-registry automated BioContainers addition for midas"
config: {"url": "https://biocontainers.pro/tools/midas", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for midas", "latest": {"1.3.2--pyh7cba7a3_7": "sha256:793db870709e8cd267042ff633a6f20b0662b52f44a6c8f4745a9a48c5d02a49"}, "tags": {"1.3.2--pyh5e36f6f_6": "sha256:f9d363d882658bf7d90aff3a406166b7e8b4ec20846d516189d13470ca1ff122", "1.3.2--pyh7cba7a3_7": "sha256:793db870709e8cd267042ff633a6f20b0662b52f44a6c8f4745a9a48c5d02a49"}, "docker": "quay.io/biocontainers/midas", "aliases": {"build_midas_db.py": "/usr/local/bin/build_midas_db.py", "call_consensus.py": "/usr/local/bin/call_consensus.py", "compare_genes.py": "/usr/local/bin/compare_genes.py", "hs-blastn": "/usr/local/bin/hs-blastn", "merge_midas.py": "/usr/local/bin/merge_midas.py", "query_by_compound.py": "/usr/local/bin/query_by_compound.py", "run_midas.py": "/usr/local/bin/run_midas.py", "snp_diversity.py": "/usr/local/bin/snp_diversity.py", "strain_tracking.py": "/usr/local/bin/strain_tracking.py", "CA.pm": "/usr/local/bin/CA.pm", "cacert.pem": "/usr/local/bin/cacert.pem", "index-themes": "/usr/local/bin/index-themes", "fetch-extras": "/usr/local/bin/fetch-extras", "go.mod": "/usr/local/bin/go.mod", "go.sum": "/usr/local/bin/go.sum", "hlp-xtract.txt": "/usr/local/bin/hlp-xtract.txt", "index-extras": "/usr/local/bin/index-extras", "pm-collect": "/usr/local/bin/pm-collect", "readme.pdf": "/usr/local/bin/readme.pdf"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/midas.
shpc-registry automated BioContainers addition for midas
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/midas
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/midas:1.3.2--pyh7cba7a3_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/midas/1.3.2--pyh7cba7a3_7
$ module help quay.io/biocontainers/midas/1.3.2--pyh7cba7a3_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### midas-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### midas-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### midas-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### midas-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### midas-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### midas-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### build_midas_db.py

```bash
$ singularity exec <container> /usr/local/bin/build_midas_db.py
$ podman run --it --rm --entrypoint /usr/local/bin/build_midas_db.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/build_midas_db.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### call_consensus.py

```bash
$ singularity exec <container> /usr/local/bin/call_consensus.py
$ podman run --it --rm --entrypoint /usr/local/bin/call_consensus.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/call_consensus.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compare_genes.py

```bash
$ singularity exec <container> /usr/local/bin/compare_genes.py
$ podman run --it --rm --entrypoint /usr/local/bin/compare_genes.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compare_genes.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hs-blastn

```bash
$ singularity exec <container> /usr/local/bin/hs-blastn
$ podman run --it --rm --entrypoint /usr/local/bin/hs-blastn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hs-blastn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge_midas.py

```bash
$ singularity exec <container> /usr/local/bin/merge_midas.py
$ podman run --it --rm --entrypoint /usr/local/bin/merge_midas.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge_midas.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### query_by_compound.py

```bash
$ singularity exec <container> /usr/local/bin/query_by_compound.py
$ podman run --it --rm --entrypoint /usr/local/bin/query_by_compound.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/query_by_compound.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_midas.py

```bash
$ singularity exec <container> /usr/local/bin/run_midas.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_midas.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_midas.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snp_diversity.py

```bash
$ singularity exec <container> /usr/local/bin/snp_diversity.py
$ podman run --it --rm --entrypoint /usr/local/bin/snp_diversity.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snp_diversity.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### strain_tracking.py

```bash
$ singularity exec <container> /usr/local/bin/strain_tracking.py
$ podman run --it --rm --entrypoint /usr/local/bin/strain_tracking.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/strain_tracking.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CA.pm

```bash
$ singularity exec <container> /usr/local/bin/CA.pm
$ podman run --it --rm --entrypoint /usr/local/bin/CA.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CA.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cacert.pem

```bash
$ singularity exec <container> /usr/local/bin/cacert.pem
$ podman run --it --rm --entrypoint /usr/local/bin/cacert.pem   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cacert.pem   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### index-themes

```bash
$ singularity exec <container> /usr/local/bin/index-themes
$ podman run --it --rm --entrypoint /usr/local/bin/index-themes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/index-themes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fetch-extras

```bash
$ singularity exec <container> /usr/local/bin/fetch-extras
$ podman run --it --rm --entrypoint /usr/local/bin/fetch-extras   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fetch-extras   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### go.mod

```bash
$ singularity exec <container> /usr/local/bin/go.mod
$ podman run --it --rm --entrypoint /usr/local/bin/go.mod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/go.mod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### go.sum

```bash
$ singularity exec <container> /usr/local/bin/go.sum
$ podman run --it --rm --entrypoint /usr/local/bin/go.sum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/go.sum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hlp-xtract.txt

```bash
$ singularity exec <container> /usr/local/bin/hlp-xtract.txt
$ podman run --it --rm --entrypoint /usr/local/bin/hlp-xtract.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hlp-xtract.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### index-extras

```bash
$ singularity exec <container> /usr/local/bin/index-extras
$ podman run --it --rm --entrypoint /usr/local/bin/index-extras   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/index-extras   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pm-collect

```bash
$ singularity exec <container> /usr/local/bin/pm-collect
$ podman run --it --rm --entrypoint /usr/local/bin/pm-collect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pm-collect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### readme.pdf

```bash
$ singularity exec <container> /usr/local/bin/readme.pdf
$ podman run --it --rm --entrypoint /usr/local/bin/readme.pdf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/readme.pdf   -v ${PWD} -w ${PWD} <container> -c " $@"
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
---
layout: container
name:  "quay.io/biocontainers/codan"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/codan/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/codan/container.yaml"
updated_at: "2024-02-29 03:06:59.832440"
latest: "1.2--h9ee0642_0"
container_url: "https://biocontainers.pro/tools/codan"
aliases:
 - "codan.py"
 - "fasta_to_tops"
 - "predict"
 - "tops-viterbi_decoding"
 - "bp_pairwise_kaks.pl"
 - "bp_search2BSML.pl"
 - "CA.pm"
 - "cacert.pem"
 - "index-themes"
 - "bp_aacomp.pl"
 - "bp_biofetch_genbank_proxy.pl"
 - "bp_bioflat_index.pl"
 - "bp_biogetseq.pl"
 - "bp_blast2tree.pl"
versions:
 - "1.2--h9ee0642_0"
description: "shpc-registry automated BioContainers addition for codan"
config: {"url": "https://biocontainers.pro/tools/codan", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for codan", "latest": {"1.2--h9ee0642_0": "sha256:bd79add0674f98a3490c9f21add769e8fb833062232b9d6e0d58f76bea73307b"}, "tags": {"1.2--h9ee0642_0": "sha256:bd79add0674f98a3490c9f21add769e8fb833062232b9d6e0d58f76bea73307b"}, "docker": "quay.io/biocontainers/codan", "aliases": {"codan.py": "/usr/local/bin/codan.py", "fasta_to_tops": "/usr/local/bin/fasta_to_tops", "predict": "/usr/local/bin/predict", "tops-viterbi_decoding": "/usr/local/bin/tops-viterbi_decoding", "bp_pairwise_kaks.pl": "/usr/local/bin/bp_pairwise_kaks.pl", "bp_search2BSML.pl": "/usr/local/bin/bp_search2BSML.pl", "CA.pm": "/usr/local/bin/CA.pm", "cacert.pem": "/usr/local/bin/cacert.pem", "index-themes": "/usr/local/bin/index-themes", "bp_aacomp.pl": "/usr/local/bin/bp_aacomp.pl", "bp_biofetch_genbank_proxy.pl": "/usr/local/bin/bp_biofetch_genbank_proxy.pl", "bp_bioflat_index.pl": "/usr/local/bin/bp_bioflat_index.pl", "bp_biogetseq.pl": "/usr/local/bin/bp_biogetseq.pl", "bp_blast2tree.pl": "/usr/local/bin/bp_blast2tree.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/codan.
shpc-registry automated BioContainers addition for codan
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/codan
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/codan:1.2--h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/codan/1.2--h9ee0642_0
$ module help quay.io/biocontainers/codan/1.2--h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### codan-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### codan-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### codan-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### codan-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### codan-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### codan-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### codan.py

```bash
$ singularity exec <container> /usr/local/bin/codan.py
$ podman run --it --rm --entrypoint /usr/local/bin/codan.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/codan.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta_to_tops

```bash
$ singularity exec <container> /usr/local/bin/fasta_to_tops
$ podman run --it --rm --entrypoint /usr/local/bin/fasta_to_tops   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta_to_tops   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### predict

```bash
$ singularity exec <container> /usr/local/bin/predict
$ podman run --it --rm --entrypoint /usr/local/bin/predict   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/predict   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tops-viterbi_decoding

```bash
$ singularity exec <container> /usr/local/bin/tops-viterbi_decoding
$ podman run --it --rm --entrypoint /usr/local/bin/tops-viterbi_decoding   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tops-viterbi_decoding   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_pairwise_kaks.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_pairwise_kaks.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_pairwise_kaks.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_pairwise_kaks.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_search2BSML.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_search2BSML.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_search2BSML.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_search2BSML.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### bp_aacomp.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_aacomp.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_aacomp.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_aacomp.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_biofetch_genbank_proxy.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_biofetch_genbank_proxy.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_biofetch_genbank_proxy.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_biofetch_genbank_proxy.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_bioflat_index.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_bioflat_index.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_bioflat_index.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_bioflat_index.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_biogetseq.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_biogetseq.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_biogetseq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_biogetseq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_blast2tree.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_blast2tree.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_blast2tree.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_blast2tree.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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
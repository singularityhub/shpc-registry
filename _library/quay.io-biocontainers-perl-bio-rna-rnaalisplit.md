---
layout: container
name:  "quay.io/biocontainers/perl-bio-rna-rnaalisplit"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-bio-rna-rnaalisplit/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-bio-rna-rnaalisplit/container.yaml"
updated_at: "2023-11-16 02:36:36.046250"
latest: "0.11--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/perl-bio-rna-rnaalisplit"
aliases:
 - "FUNCS.pm"
 - "MetamakeDemos.pl"
 - "PDBFUNCS.pm"
 - "R-scape"
 - "R-scape-sim"
 - "R-scape-sim-nobps"
 - "R-view"
 - "RNAalisplit.pl"
 - "RNAz"
 - "SelectSubFamilyFromStockholm.pl"
 - "Stockholm.pm"
 - "appcov"
 - "eval_alignment.pl"
 - "msafilter"
 - "pdb_parse.pl"
 - "r2r"
 - "r2r_msa_comply.pl"
 - "rnazAnnotate.pl"
 - "rnazBEDsort.pl"
 - "rnazBEDstats.pl"
 - "rnazBlast.pl"
 - "rnazCluster.pl"
 - "rnazFilter.pl"
 - "rnazIndex.pl"
 - "rnazMAF2BED.pl"
 - "rnazRandomizeAln.pl"
 - "rnazSelectSeqs.pl"
 - "rnazSort.pl"
 - "rnazWindow.pl"
 - "bp_pairwise_kaks.pl"
 - "bp_search2BSML.pl"
 - "gnuplot"
 - "AnalyseDists"
 - "AnalyseSeqs"
 - "RNAlocmin"
 - "RNApvmin"
 - "b2ct"
 - "ct2db"
 - "kinwalker"
versions:
 - "v0.09--pl526_0"
 - "0.11--pl5321hdfd78af_0"
description: "shpc-registry automated BioContainers addition for perl-bio-rna-rnaalisplit"
config: {"url": "https://biocontainers.pro/tools/perl-bio-rna-rnaalisplit", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-bio-rna-rnaalisplit", "latest": {"0.11--pl5321hdfd78af_0": "sha256:118298c8e9d71d83f3aeb47fd8409ab92907324d219b6b3420cafa7929ab9ffa"}, "tags": {"v0.09--pl526_0": "sha256:da30c3038969f787477ac7d57e02dbcefbf8f4db16e8f7555b9efb422f369425", "0.11--pl5321hdfd78af_0": "sha256:118298c8e9d71d83f3aeb47fd8409ab92907324d219b6b3420cafa7929ab9ffa"}, "docker": "quay.io/biocontainers/perl-bio-rna-rnaalisplit", "aliases": {"FUNCS.pm": "/usr/local/bin/FUNCS.pm", "MetamakeDemos.pl": "/usr/local/bin/MetamakeDemos.pl", "PDBFUNCS.pm": "/usr/local/bin/PDBFUNCS.pm", "R-scape": "/usr/local/bin/R-scape", "R-scape-sim": "/usr/local/bin/R-scape-sim", "R-scape-sim-nobps": "/usr/local/bin/R-scape-sim-nobps", "R-view": "/usr/local/bin/R-view", "RNAalisplit.pl": "/usr/local/bin/RNAalisplit.pl", "RNAz": "/usr/local/bin/RNAz", "SelectSubFamilyFromStockholm.pl": "/usr/local/bin/SelectSubFamilyFromStockholm.pl", "Stockholm.pm": "/usr/local/bin/Stockholm.pm", "appcov": "/usr/local/bin/appcov", "eval_alignment.pl": "/usr/local/bin/eval_alignment.pl", "msafilter": "/usr/local/bin/msafilter", "pdb_parse.pl": "/usr/local/bin/pdb_parse.pl", "r2r": "/usr/local/bin/r2r", "r2r_msa_comply.pl": "/usr/local/bin/r2r_msa_comply.pl", "rnazAnnotate.pl": "/usr/local/bin/rnazAnnotate.pl", "rnazBEDsort.pl": "/usr/local/bin/rnazBEDsort.pl", "rnazBEDstats.pl": "/usr/local/bin/rnazBEDstats.pl", "rnazBlast.pl": "/usr/local/bin/rnazBlast.pl", "rnazCluster.pl": "/usr/local/bin/rnazCluster.pl", "rnazFilter.pl": "/usr/local/bin/rnazFilter.pl", "rnazIndex.pl": "/usr/local/bin/rnazIndex.pl", "rnazMAF2BED.pl": "/usr/local/bin/rnazMAF2BED.pl", "rnazRandomizeAln.pl": "/usr/local/bin/rnazRandomizeAln.pl", "rnazSelectSeqs.pl": "/usr/local/bin/rnazSelectSeqs.pl", "rnazSort.pl": "/usr/local/bin/rnazSort.pl", "rnazWindow.pl": "/usr/local/bin/rnazWindow.pl", "bp_pairwise_kaks.pl": "/usr/local/bin/bp_pairwise_kaks.pl", "bp_search2BSML.pl": "/usr/local/bin/bp_search2BSML.pl", "gnuplot": "/usr/local/bin/gnuplot", "AnalyseDists": "/usr/local/bin/AnalyseDists", "AnalyseSeqs": "/usr/local/bin/AnalyseSeqs", "RNAlocmin": "/usr/local/bin/RNAlocmin", "RNApvmin": "/usr/local/bin/RNApvmin", "b2ct": "/usr/local/bin/b2ct", "ct2db": "/usr/local/bin/ct2db", "kinwalker": "/usr/local/bin/kinwalker"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-bio-rna-rnaalisplit.
shpc-registry automated BioContainers addition for perl-bio-rna-rnaalisplit
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-bio-rna-rnaalisplit
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-bio-rna-rnaalisplit:0.11--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-bio-rna-rnaalisplit/0.11--pl5321hdfd78af_0
$ module help quay.io/biocontainers/perl-bio-rna-rnaalisplit/0.11--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-bio-rna-rnaalisplit-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-bio-rna-rnaalisplit-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-bio-rna-rnaalisplit-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-bio-rna-rnaalisplit-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-bio-rna-rnaalisplit-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-bio-rna-rnaalisplit-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### FUNCS.pm

```bash
$ singularity exec <container> /usr/local/bin/FUNCS.pm
$ podman run --it --rm --entrypoint /usr/local/bin/FUNCS.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FUNCS.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MetamakeDemos.pl

```bash
$ singularity exec <container> /usr/local/bin/MetamakeDemos.pl
$ podman run --it --rm --entrypoint /usr/local/bin/MetamakeDemos.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MetamakeDemos.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PDBFUNCS.pm

```bash
$ singularity exec <container> /usr/local/bin/PDBFUNCS.pm
$ podman run --it --rm --entrypoint /usr/local/bin/PDBFUNCS.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PDBFUNCS.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### R-scape

```bash
$ singularity exec <container> /usr/local/bin/R-scape
$ podman run --it --rm --entrypoint /usr/local/bin/R-scape   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/R-scape   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### R-scape-sim

```bash
$ singularity exec <container> /usr/local/bin/R-scape-sim
$ podman run --it --rm --entrypoint /usr/local/bin/R-scape-sim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/R-scape-sim   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### R-scape-sim-nobps

```bash
$ singularity exec <container> /usr/local/bin/R-scape-sim-nobps
$ podman run --it --rm --entrypoint /usr/local/bin/R-scape-sim-nobps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/R-scape-sim-nobps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### R-view

```bash
$ singularity exec <container> /usr/local/bin/R-view
$ podman run --it --rm --entrypoint /usr/local/bin/R-view   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/R-view   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAalisplit.pl

```bash
$ singularity exec <container> /usr/local/bin/RNAalisplit.pl
$ podman run --it --rm --entrypoint /usr/local/bin/RNAalisplit.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAalisplit.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAz

```bash
$ singularity exec <container> /usr/local/bin/RNAz
$ podman run --it --rm --entrypoint /usr/local/bin/RNAz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SelectSubFamilyFromStockholm.pl

```bash
$ singularity exec <container> /usr/local/bin/SelectSubFamilyFromStockholm.pl
$ podman run --it --rm --entrypoint /usr/local/bin/SelectSubFamilyFromStockholm.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SelectSubFamilyFromStockholm.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Stockholm.pm

```bash
$ singularity exec <container> /usr/local/bin/Stockholm.pm
$ podman run --it --rm --entrypoint /usr/local/bin/Stockholm.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Stockholm.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### appcov

```bash
$ singularity exec <container> /usr/local/bin/appcov
$ podman run --it --rm --entrypoint /usr/local/bin/appcov   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/appcov   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eval_alignment.pl

```bash
$ singularity exec <container> /usr/local/bin/eval_alignment.pl
$ podman run --it --rm --entrypoint /usr/local/bin/eval_alignment.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eval_alignment.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### msafilter

```bash
$ singularity exec <container> /usr/local/bin/msafilter
$ podman run --it --rm --entrypoint /usr/local/bin/msafilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/msafilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdb_parse.pl

```bash
$ singularity exec <container> /usr/local/bin/pdb_parse.pl
$ podman run --it --rm --entrypoint /usr/local/bin/pdb_parse.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdb_parse.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### r2r

```bash
$ singularity exec <container> /usr/local/bin/r2r
$ podman run --it --rm --entrypoint /usr/local/bin/r2r   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/r2r   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### r2r_msa_comply.pl

```bash
$ singularity exec <container> /usr/local/bin/r2r_msa_comply.pl
$ podman run --it --rm --entrypoint /usr/local/bin/r2r_msa_comply.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/r2r_msa_comply.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rnazAnnotate.pl

```bash
$ singularity exec <container> /usr/local/bin/rnazAnnotate.pl
$ podman run --it --rm --entrypoint /usr/local/bin/rnazAnnotate.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnazAnnotate.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rnazBEDsort.pl

```bash
$ singularity exec <container> /usr/local/bin/rnazBEDsort.pl
$ podman run --it --rm --entrypoint /usr/local/bin/rnazBEDsort.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnazBEDsort.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rnazBEDstats.pl

```bash
$ singularity exec <container> /usr/local/bin/rnazBEDstats.pl
$ podman run --it --rm --entrypoint /usr/local/bin/rnazBEDstats.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnazBEDstats.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rnazBlast.pl

```bash
$ singularity exec <container> /usr/local/bin/rnazBlast.pl
$ podman run --it --rm --entrypoint /usr/local/bin/rnazBlast.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnazBlast.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rnazCluster.pl

```bash
$ singularity exec <container> /usr/local/bin/rnazCluster.pl
$ podman run --it --rm --entrypoint /usr/local/bin/rnazCluster.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnazCluster.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rnazFilter.pl

```bash
$ singularity exec <container> /usr/local/bin/rnazFilter.pl
$ podman run --it --rm --entrypoint /usr/local/bin/rnazFilter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnazFilter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rnazIndex.pl

```bash
$ singularity exec <container> /usr/local/bin/rnazIndex.pl
$ podman run --it --rm --entrypoint /usr/local/bin/rnazIndex.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnazIndex.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rnazMAF2BED.pl

```bash
$ singularity exec <container> /usr/local/bin/rnazMAF2BED.pl
$ podman run --it --rm --entrypoint /usr/local/bin/rnazMAF2BED.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnazMAF2BED.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rnazRandomizeAln.pl

```bash
$ singularity exec <container> /usr/local/bin/rnazRandomizeAln.pl
$ podman run --it --rm --entrypoint /usr/local/bin/rnazRandomizeAln.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnazRandomizeAln.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rnazSelectSeqs.pl

```bash
$ singularity exec <container> /usr/local/bin/rnazSelectSeqs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/rnazSelectSeqs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnazSelectSeqs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rnazSort.pl

```bash
$ singularity exec <container> /usr/local/bin/rnazSort.pl
$ podman run --it --rm --entrypoint /usr/local/bin/rnazSort.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnazSort.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rnazWindow.pl

```bash
$ singularity exec <container> /usr/local/bin/rnazWindow.pl
$ podman run --it --rm --entrypoint /usr/local/bin/rnazWindow.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnazWindow.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### gnuplot

```bash
$ singularity exec <container> /usr/local/bin/gnuplot
$ podman run --it --rm --entrypoint /usr/local/bin/gnuplot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gnuplot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### AnalyseDists

```bash
$ singularity exec <container> /usr/local/bin/AnalyseDists
$ podman run --it --rm --entrypoint /usr/local/bin/AnalyseDists   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AnalyseDists   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### AnalyseSeqs

```bash
$ singularity exec <container> /usr/local/bin/AnalyseSeqs
$ podman run --it --rm --entrypoint /usr/local/bin/AnalyseSeqs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AnalyseSeqs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAlocmin

```bash
$ singularity exec <container> /usr/local/bin/RNAlocmin
$ podman run --it --rm --entrypoint /usr/local/bin/RNAlocmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAlocmin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNApvmin

```bash
$ singularity exec <container> /usr/local/bin/RNApvmin
$ podman run --it --rm --entrypoint /usr/local/bin/RNApvmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNApvmin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### b2ct

```bash
$ singularity exec <container> /usr/local/bin/b2ct
$ podman run --it --rm --entrypoint /usr/local/bin/b2ct   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/b2ct   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ct2db

```bash
$ singularity exec <container> /usr/local/bin/ct2db
$ podman run --it --rm --entrypoint /usr/local/bin/ct2db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ct2db   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kinwalker

```bash
$ singularity exec <container> /usr/local/bin/kinwalker
$ podman run --it --rm --entrypoint /usr/local/bin/kinwalker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kinwalker   -v ${PWD} -w ${PWD} <container> -c " $@"
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
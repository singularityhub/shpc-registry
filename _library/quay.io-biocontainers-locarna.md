---
layout: container
name:  "quay.io/biocontainers/locarna"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/locarna/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/locarna/container.yaml"
updated_at: "2024-09-12 03:23:39.686115"
latest: "2.0.1--pl5321h4ac6f70_0"
container_url: "https://biocontainers.pro/tools/locarna"
aliases:
 - "LocARNA_RNAz.pm"
 - "RNAz.pm"
 - "aln-seqs.pl"
 - "aln2fa.pl"
 - "alnsel.pl"
 - "average-dot.pl"
 - "benchmark-plot.R"
 - "dot2pp"
 - "exparna_p"
 - "exploc_p"
 - "gen-reliab-dot.pl"
 - "locarna"
 - "locarna-mea.pl"
 - "locarna-motif-scan"
 - "locarna_deviation"
 - "locarna_mcc"
 - "locarna_p"
 - "locarna_rnafold_pp"
 - "locarnap-predict-and-plot.pl"
 - "locarnap-realign-all.pl"
 - "locarnap-revcomp.pl"
 - "locarnap-revisit-RNAz-hits.pl"
 - "locarnap_fit"
 - "locarnate"
 - "mlocarna"
 - "mlocarna_nnames"
 - "plot-bmprobs"
 - "pp2dot"
 - "reliability-profile.pl"
 - "ribosum2cc"
 - "sparse"
 - "AnalyseDists"
 - "AnalyseSeqs"
 - "RNAlocmin"
 - "RNApvmin"
 - "b2ct"
 - "ct2db"
 - "kinwalker"
 - "popt"
 - "RNA2Dfold"
 - "RNALalifold"
versions:
 - "2.0.0RC8--h9f5acd7_2"
 - "2.0.0RC10--pl5321h9f5acd7_1"
 - "2.0.1--pl5321h4ac6f70_0"
description: "shpc-registry automated BioContainers addition for locarna"
config: {"url": "https://biocontainers.pro/tools/locarna", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for locarna", "latest": {"2.0.1--pl5321h4ac6f70_0": "sha256:02dea7b5619e5287112f917417bcc92f26afc79a181f59c2b891d52452892fe0"}, "tags": {"2.0.0RC8--h9f5acd7_2": "sha256:8268570b9afd9615850876b18e1732357bf1ee8a27db61c281d6f4aa30334920", "2.0.0RC10--pl5321h9f5acd7_1": "sha256:aceba0e44a9f2253cf544ca3b73d390059306a5b7985a0ae178053de862cd473", "2.0.1--pl5321h4ac6f70_0": "sha256:02dea7b5619e5287112f917417bcc92f26afc79a181f59c2b891d52452892fe0"}, "docker": "quay.io/biocontainers/locarna", "aliases": {"LocARNA_RNAz.pm": "/usr/local/bin/LocARNA_RNAz.pm", "RNAz.pm": "/usr/local/bin/RNAz.pm", "aln-seqs.pl": "/usr/local/bin/aln-seqs.pl", "aln2fa.pl": "/usr/local/bin/aln2fa.pl", "alnsel.pl": "/usr/local/bin/alnsel.pl", "average-dot.pl": "/usr/local/bin/average-dot.pl", "benchmark-plot.R": "/usr/local/bin/benchmark-plot.R", "dot2pp": "/usr/local/bin/dot2pp", "exparna_p": "/usr/local/bin/exparna_p", "exploc_p": "/usr/local/bin/exploc_p", "gen-reliab-dot.pl": "/usr/local/bin/gen-reliab-dot.pl", "locarna": "/usr/local/bin/locarna", "locarna-mea.pl": "/usr/local/bin/locarna-mea.pl", "locarna-motif-scan": "/usr/local/bin/locarna-motif-scan", "locarna_deviation": "/usr/local/bin/locarna_deviation", "locarna_mcc": "/usr/local/bin/locarna_mcc", "locarna_p": "/usr/local/bin/locarna_p", "locarna_rnafold_pp": "/usr/local/bin/locarna_rnafold_pp", "locarnap-predict-and-plot.pl": "/usr/local/bin/locarnap-predict-and-plot.pl", "locarnap-realign-all.pl": "/usr/local/bin/locarnap-realign-all.pl", "locarnap-revcomp.pl": "/usr/local/bin/locarnap-revcomp.pl", "locarnap-revisit-RNAz-hits.pl": "/usr/local/bin/locarnap-revisit-RNAz-hits.pl", "locarnap_fit": "/usr/local/bin/locarnap_fit", "locarnate": "/usr/local/bin/locarnate", "mlocarna": "/usr/local/bin/mlocarna", "mlocarna_nnames": "/usr/local/bin/mlocarna_nnames", "plot-bmprobs": "/usr/local/bin/plot-bmprobs", "pp2dot": "/usr/local/bin/pp2dot", "reliability-profile.pl": "/usr/local/bin/reliability-profile.pl", "ribosum2cc": "/usr/local/bin/ribosum2cc", "sparse": "/usr/local/bin/sparse", "AnalyseDists": "/usr/local/bin/AnalyseDists", "AnalyseSeqs": "/usr/local/bin/AnalyseSeqs", "RNAlocmin": "/usr/local/bin/RNAlocmin", "RNApvmin": "/usr/local/bin/RNApvmin", "b2ct": "/usr/local/bin/b2ct", "ct2db": "/usr/local/bin/ct2db", "kinwalker": "/usr/local/bin/kinwalker", "popt": "/usr/local/bin/popt", "RNA2Dfold": "/usr/local/bin/RNA2Dfold", "RNALalifold": "/usr/local/bin/RNALalifold"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/locarna.
shpc-registry automated BioContainers addition for locarna
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/locarna
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/locarna:2.0.1--pl5321h4ac6f70_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/locarna/2.0.1--pl5321h4ac6f70_0
$ module help quay.io/biocontainers/locarna/2.0.1--pl5321h4ac6f70_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### locarna-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### locarna-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### locarna-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### locarna-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### locarna-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### locarna-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### LocARNA_RNAz.pm

```bash
$ singularity exec <container> /usr/local/bin/LocARNA_RNAz.pm
$ podman run --it --rm --entrypoint /usr/local/bin/LocARNA_RNAz.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LocARNA_RNAz.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAz.pm

```bash
$ singularity exec <container> /usr/local/bin/RNAz.pm
$ podman run --it --rm --entrypoint /usr/local/bin/RNAz.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAz.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aln-seqs.pl

```bash
$ singularity exec <container> /usr/local/bin/aln-seqs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/aln-seqs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aln-seqs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aln2fa.pl

```bash
$ singularity exec <container> /usr/local/bin/aln2fa.pl
$ podman run --it --rm --entrypoint /usr/local/bin/aln2fa.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aln2fa.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alnsel.pl

```bash
$ singularity exec <container> /usr/local/bin/alnsel.pl
$ podman run --it --rm --entrypoint /usr/local/bin/alnsel.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alnsel.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### average-dot.pl

```bash
$ singularity exec <container> /usr/local/bin/average-dot.pl
$ podman run --it --rm --entrypoint /usr/local/bin/average-dot.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/average-dot.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### benchmark-plot.R

```bash
$ singularity exec <container> /usr/local/bin/benchmark-plot.R
$ podman run --it --rm --entrypoint /usr/local/bin/benchmark-plot.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/benchmark-plot.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dot2pp

```bash
$ singularity exec <container> /usr/local/bin/dot2pp
$ podman run --it --rm --entrypoint /usr/local/bin/dot2pp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dot2pp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exparna_p

```bash
$ singularity exec <container> /usr/local/bin/exparna_p
$ podman run --it --rm --entrypoint /usr/local/bin/exparna_p   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exparna_p   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exploc_p

```bash
$ singularity exec <container> /usr/local/bin/exploc_p
$ podman run --it --rm --entrypoint /usr/local/bin/exploc_p   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exploc_p   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gen-reliab-dot.pl

```bash
$ singularity exec <container> /usr/local/bin/gen-reliab-dot.pl
$ podman run --it --rm --entrypoint /usr/local/bin/gen-reliab-dot.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gen-reliab-dot.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### locarna

```bash
$ singularity exec <container> /usr/local/bin/locarna
$ podman run --it --rm --entrypoint /usr/local/bin/locarna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/locarna   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### locarna-mea.pl

```bash
$ singularity exec <container> /usr/local/bin/locarna-mea.pl
$ podman run --it --rm --entrypoint /usr/local/bin/locarna-mea.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/locarna-mea.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### locarna-motif-scan

```bash
$ singularity exec <container> /usr/local/bin/locarna-motif-scan
$ podman run --it --rm --entrypoint /usr/local/bin/locarna-motif-scan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/locarna-motif-scan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### locarna_deviation

```bash
$ singularity exec <container> /usr/local/bin/locarna_deviation
$ podman run --it --rm --entrypoint /usr/local/bin/locarna_deviation   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/locarna_deviation   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### locarna_mcc

```bash
$ singularity exec <container> /usr/local/bin/locarna_mcc
$ podman run --it --rm --entrypoint /usr/local/bin/locarna_mcc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/locarna_mcc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### locarna_p

```bash
$ singularity exec <container> /usr/local/bin/locarna_p
$ podman run --it --rm --entrypoint /usr/local/bin/locarna_p   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/locarna_p   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### locarna_rnafold_pp

```bash
$ singularity exec <container> /usr/local/bin/locarna_rnafold_pp
$ podman run --it --rm --entrypoint /usr/local/bin/locarna_rnafold_pp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/locarna_rnafold_pp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### locarnap-predict-and-plot.pl

```bash
$ singularity exec <container> /usr/local/bin/locarnap-predict-and-plot.pl
$ podman run --it --rm --entrypoint /usr/local/bin/locarnap-predict-and-plot.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/locarnap-predict-and-plot.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### locarnap-realign-all.pl

```bash
$ singularity exec <container> /usr/local/bin/locarnap-realign-all.pl
$ podman run --it --rm --entrypoint /usr/local/bin/locarnap-realign-all.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/locarnap-realign-all.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### locarnap-revcomp.pl

```bash
$ singularity exec <container> /usr/local/bin/locarnap-revcomp.pl
$ podman run --it --rm --entrypoint /usr/local/bin/locarnap-revcomp.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/locarnap-revcomp.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### locarnap-revisit-RNAz-hits.pl

```bash
$ singularity exec <container> /usr/local/bin/locarnap-revisit-RNAz-hits.pl
$ podman run --it --rm --entrypoint /usr/local/bin/locarnap-revisit-RNAz-hits.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/locarnap-revisit-RNAz-hits.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### locarnap_fit

```bash
$ singularity exec <container> /usr/local/bin/locarnap_fit
$ podman run --it --rm --entrypoint /usr/local/bin/locarnap_fit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/locarnap_fit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### locarnate

```bash
$ singularity exec <container> /usr/local/bin/locarnate
$ podman run --it --rm --entrypoint /usr/local/bin/locarnate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/locarnate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mlocarna

```bash
$ singularity exec <container> /usr/local/bin/mlocarna
$ podman run --it --rm --entrypoint /usr/local/bin/mlocarna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mlocarna   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mlocarna_nnames

```bash
$ singularity exec <container> /usr/local/bin/mlocarna_nnames
$ podman run --it --rm --entrypoint /usr/local/bin/mlocarna_nnames   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mlocarna_nnames   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-bmprobs

```bash
$ singularity exec <container> /usr/local/bin/plot-bmprobs
$ podman run --it --rm --entrypoint /usr/local/bin/plot-bmprobs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-bmprobs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pp2dot

```bash
$ singularity exec <container> /usr/local/bin/pp2dot
$ podman run --it --rm --entrypoint /usr/local/bin/pp2dot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pp2dot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### reliability-profile.pl

```bash
$ singularity exec <container> /usr/local/bin/reliability-profile.pl
$ podman run --it --rm --entrypoint /usr/local/bin/reliability-profile.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/reliability-profile.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ribosum2cc

```bash
$ singularity exec <container> /usr/local/bin/ribosum2cc
$ podman run --it --rm --entrypoint /usr/local/bin/ribosum2cc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ribosum2cc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sparse

```bash
$ singularity exec <container> /usr/local/bin/sparse
$ podman run --it --rm --entrypoint /usr/local/bin/sparse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sparse   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### popt

```bash
$ singularity exec <container> /usr/local/bin/popt
$ podman run --it --rm --entrypoint /usr/local/bin/popt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/popt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNA2Dfold

```bash
$ singularity exec <container> /usr/local/bin/RNA2Dfold
$ podman run --it --rm --entrypoint /usr/local/bin/RNA2Dfold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNA2Dfold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNALalifold

```bash
$ singularity exec <container> /usr/local/bin/RNALalifold
$ podman run --it --rm --entrypoint /usr/local/bin/RNALalifold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNALalifold   -v ${PWD} -w ${PWD} <container> -c " $@"
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
---
layout: container
name:  "quay.io/biocontainers/metamaps"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metamaps/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/metamaps/container.yaml"
updated_at: "2023-12-29 02:46:16.322564"
latest: "0.1.98102e9--h21ec9f0_2"
container_url: "https://biocontainers.pro/tools/metamaps"
aliases:
 - "DBinfo.pl"
 - "annotateRefSeqSequencesWithUniqueTaxonIDs.pl"
 - "benchmarkInference.pl"
 - "buildDB.pl"
 - "callCentrifugeOnConvertedDB.pl"
 - "callKraken2OnConvertedDB.pl"
 - "callKrakenOnConvertedDB.pl"
 - "combineAndAnnotateReferences.pl"
 - "convertMetaMapsToCentrifuge.pl"
 - "convertMetaMapsToKraken.pl"
 - "convertMetaMapsToMash.pl"
 - "doPlots.R"
 - "downloadRefSeq.pl"
 - "estimateSelfSimilarity.pl"
 - "firstQuartileScore.pl"
 - "fixSimulationStore.pl"
 - "geneLevelAnalysis.pl"
 - "metamaps"
 - "plotMappingSummary.R"
 - "plotUnknownResults.R"
 - "shortenContigIDs.pl"
 - "simulate.pl"
 - "test2.pl"
 - "validateDB.pl"
 - "lwp-download"
 - "lwp-dump"
 - "lwp-mirror"
 - "lwp-request"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "0.1.98102e9--h7ff8a90_1"
 - "0.1.98102e9--h21ec9f0_2"
description: "shpc-registry automated BioContainers addition for metamaps"
config: {"url": "https://biocontainers.pro/tools/metamaps", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for metamaps", "latest": {"0.1.98102e9--h21ec9f0_2": "sha256:57432c76f40209806c7c559a27f987ec503a9adfae9a1658471f0f108cf593e6"}, "tags": {"0.1.98102e9--h7ff8a90_1": "sha256:ba772dcb091145643e68054cf20a0b9b0c28148e4c39cd73f882045efd796692", "0.1.98102e9--h21ec9f0_2": "sha256:57432c76f40209806c7c559a27f987ec503a9adfae9a1658471f0f108cf593e6"}, "docker": "quay.io/biocontainers/metamaps", "aliases": {"DBinfo.pl": "/usr/local/bin/DBinfo.pl", "annotateRefSeqSequencesWithUniqueTaxonIDs.pl": "/usr/local/bin/annotateRefSeqSequencesWithUniqueTaxonIDs.pl", "benchmarkInference.pl": "/usr/local/bin/benchmarkInference.pl", "buildDB.pl": "/usr/local/bin/buildDB.pl", "callCentrifugeOnConvertedDB.pl": "/usr/local/bin/callCentrifugeOnConvertedDB.pl", "callKraken2OnConvertedDB.pl": "/usr/local/bin/callKraken2OnConvertedDB.pl", "callKrakenOnConvertedDB.pl": "/usr/local/bin/callKrakenOnConvertedDB.pl", "combineAndAnnotateReferences.pl": "/usr/local/bin/combineAndAnnotateReferences.pl", "convertMetaMapsToCentrifuge.pl": "/usr/local/bin/convertMetaMapsToCentrifuge.pl", "convertMetaMapsToKraken.pl": "/usr/local/bin/convertMetaMapsToKraken.pl", "convertMetaMapsToMash.pl": "/usr/local/bin/convertMetaMapsToMash.pl", "doPlots.R": "/usr/local/bin/doPlots.R", "downloadRefSeq.pl": "/usr/local/bin/downloadRefSeq.pl", "estimateSelfSimilarity.pl": "/usr/local/bin/estimateSelfSimilarity.pl", "firstQuartileScore.pl": "/usr/local/bin/firstQuartileScore.pl", "fixSimulationStore.pl": "/usr/local/bin/fixSimulationStore.pl", "geneLevelAnalysis.pl": "/usr/local/bin/geneLevelAnalysis.pl", "metamaps": "/usr/local/bin/metamaps", "plotMappingSummary.R": "/usr/local/bin/plotMappingSummary.R", "plotUnknownResults.R": "/usr/local/bin/plotUnknownResults.R", "shortenContigIDs.pl": "/usr/local/bin/shortenContigIDs.pl", "simulate.pl": "/usr/local/bin/simulate.pl", "test2.pl": "/usr/local/bin/test2.pl", "validateDB.pl": "/usr/local/bin/validateDB.pl", "lwp-download": "/usr/local/bin/lwp-download", "lwp-dump": "/usr/local/bin/lwp-dump", "lwp-mirror": "/usr/local/bin/lwp-mirror", "lwp-request": "/usr/local/bin/lwp-request", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metamaps.
shpc-registry automated BioContainers addition for metamaps
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metamaps
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metamaps:0.1.98102e9--h21ec9f0_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metamaps/0.1.98102e9--h21ec9f0_2
$ module help quay.io/biocontainers/metamaps/0.1.98102e9--h21ec9f0_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metamaps-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metamaps-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metamaps-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metamaps-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metamaps-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metamaps-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### DBinfo.pl

```bash
$ singularity exec <container> /usr/local/bin/DBinfo.pl
$ podman run --it --rm --entrypoint /usr/local/bin/DBinfo.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DBinfo.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotateRefSeqSequencesWithUniqueTaxonIDs.pl

```bash
$ singularity exec <container> /usr/local/bin/annotateRefSeqSequencesWithUniqueTaxonIDs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/annotateRefSeqSequencesWithUniqueTaxonIDs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotateRefSeqSequencesWithUniqueTaxonIDs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### benchmarkInference.pl

```bash
$ singularity exec <container> /usr/local/bin/benchmarkInference.pl
$ podman run --it --rm --entrypoint /usr/local/bin/benchmarkInference.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/benchmarkInference.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### buildDB.pl

```bash
$ singularity exec <container> /usr/local/bin/buildDB.pl
$ podman run --it --rm --entrypoint /usr/local/bin/buildDB.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/buildDB.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### callCentrifugeOnConvertedDB.pl

```bash
$ singularity exec <container> /usr/local/bin/callCentrifugeOnConvertedDB.pl
$ podman run --it --rm --entrypoint /usr/local/bin/callCentrifugeOnConvertedDB.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/callCentrifugeOnConvertedDB.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### callKraken2OnConvertedDB.pl

```bash
$ singularity exec <container> /usr/local/bin/callKraken2OnConvertedDB.pl
$ podman run --it --rm --entrypoint /usr/local/bin/callKraken2OnConvertedDB.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/callKraken2OnConvertedDB.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### callKrakenOnConvertedDB.pl

```bash
$ singularity exec <container> /usr/local/bin/callKrakenOnConvertedDB.pl
$ podman run --it --rm --entrypoint /usr/local/bin/callKrakenOnConvertedDB.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/callKrakenOnConvertedDB.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combineAndAnnotateReferences.pl

```bash
$ singularity exec <container> /usr/local/bin/combineAndAnnotateReferences.pl
$ podman run --it --rm --entrypoint /usr/local/bin/combineAndAnnotateReferences.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combineAndAnnotateReferences.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convertMetaMapsToCentrifuge.pl

```bash
$ singularity exec <container> /usr/local/bin/convertMetaMapsToCentrifuge.pl
$ podman run --it --rm --entrypoint /usr/local/bin/convertMetaMapsToCentrifuge.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convertMetaMapsToCentrifuge.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convertMetaMapsToKraken.pl

```bash
$ singularity exec <container> /usr/local/bin/convertMetaMapsToKraken.pl
$ podman run --it --rm --entrypoint /usr/local/bin/convertMetaMapsToKraken.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convertMetaMapsToKraken.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convertMetaMapsToMash.pl

```bash
$ singularity exec <container> /usr/local/bin/convertMetaMapsToMash.pl
$ podman run --it --rm --entrypoint /usr/local/bin/convertMetaMapsToMash.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convertMetaMapsToMash.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### doPlots.R

```bash
$ singularity exec <container> /usr/local/bin/doPlots.R
$ podman run --it --rm --entrypoint /usr/local/bin/doPlots.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/doPlots.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### downloadRefSeq.pl

```bash
$ singularity exec <container> /usr/local/bin/downloadRefSeq.pl
$ podman run --it --rm --entrypoint /usr/local/bin/downloadRefSeq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/downloadRefSeq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### estimateSelfSimilarity.pl

```bash
$ singularity exec <container> /usr/local/bin/estimateSelfSimilarity.pl
$ podman run --it --rm --entrypoint /usr/local/bin/estimateSelfSimilarity.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/estimateSelfSimilarity.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### firstQuartileScore.pl

```bash
$ singularity exec <container> /usr/local/bin/firstQuartileScore.pl
$ podman run --it --rm --entrypoint /usr/local/bin/firstQuartileScore.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/firstQuartileScore.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fixSimulationStore.pl

```bash
$ singularity exec <container> /usr/local/bin/fixSimulationStore.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fixSimulationStore.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fixSimulationStore.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### geneLevelAnalysis.pl

```bash
$ singularity exec <container> /usr/local/bin/geneLevelAnalysis.pl
$ podman run --it --rm --entrypoint /usr/local/bin/geneLevelAnalysis.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/geneLevelAnalysis.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metamaps

```bash
$ singularity exec <container> /usr/local/bin/metamaps
$ podman run --it --rm --entrypoint /usr/local/bin/metamaps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metamaps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotMappingSummary.R

```bash
$ singularity exec <container> /usr/local/bin/plotMappingSummary.R
$ podman run --it --rm --entrypoint /usr/local/bin/plotMappingSummary.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotMappingSummary.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotUnknownResults.R

```bash
$ singularity exec <container> /usr/local/bin/plotUnknownResults.R
$ podman run --it --rm --entrypoint /usr/local/bin/plotUnknownResults.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotUnknownResults.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shortenContigIDs.pl

```bash
$ singularity exec <container> /usr/local/bin/shortenContigIDs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/shortenContigIDs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shortenContigIDs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### simulate.pl

```bash
$ singularity exec <container> /usr/local/bin/simulate.pl
$ podman run --it --rm --entrypoint /usr/local/bin/simulate.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/simulate.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test2.pl

```bash
$ singularity exec <container> /usr/local/bin/test2.pl
$ podman run --it --rm --entrypoint /usr/local/bin/test2.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test2.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### validateDB.pl

```bash
$ singularity exec <container> /usr/local/bin/validateDB.pl
$ podman run --it --rm --entrypoint /usr/local/bin/validateDB.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/validateDB.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lwp-download

```bash
$ singularity exec <container> /usr/local/bin/lwp-download
$ podman run --it --rm --entrypoint /usr/local/bin/lwp-download   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lwp-download   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lwp-dump

```bash
$ singularity exec <container> /usr/local/bin/lwp-dump
$ podman run --it --rm --entrypoint /usr/local/bin/lwp-dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lwp-dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lwp-mirror

```bash
$ singularity exec <container> /usr/local/bin/lwp-mirror
$ podman run --it --rm --entrypoint /usr/local/bin/lwp-mirror   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lwp-mirror   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lwp-request

```bash
$ singularity exec <container> /usr/local/bin/lwp-request
$ podman run --it --rm --entrypoint /usr/local/bin/lwp-request   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lwp-request   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.32.1

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.1
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamzip

```bash
$ singularity exec <container> /usr/local/bin/streamzip
$ podman run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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
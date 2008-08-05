import FWCore.ParameterSet.Config as cms

ecalBarrelClusterTask = cms.EDFilter("EBClusterTask",
    prefixME = cms.untracked.string('EcalBarrel'),
    enableCleanup = cms.untracked.bool(False),
    mergeRuns = cms.untracked.bool(False),    
    EcalRawDataCollection = cms.InputTag("ecalEBunpacker"),
    BasicClusterCollection = cms.InputTag("hybridSuperClusters","hybridBarrelBasicClusters"),
    SuperClusterCollection = cms.InputTag("correctedHybridSuperClusters"),
    reducedBarrelRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEB")
)


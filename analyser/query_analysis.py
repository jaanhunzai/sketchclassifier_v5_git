# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 11:45:06 2018

@author: s_jan001
"""
from neo4j.v1 import GraphDatabase


uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri)

####################################### Topological relations between landmarks and regions########################################

def getTotalRelations_rcc11_mm():
    params = {}
    session = driver.session()
    query ="""
       match (nm:Map)
        where nm.map_type = "metric_map"
       
        with nm 
        match (nm)-[hpr:HAS_PARTIAL_REPRESENTATION]->(nq:QCN)-[hn:HAS_NODE]->
        (nqn:QCN_Node)-[sr:SPATIAL_RELATION]->(nqn1:QCN_Node)
        where
        nq.relation_set = "RCC11" 
        return count(sr) As totalNoOfRCC11Relations_mm
        """
    totalRCC11Relations_mm= session.run (query, paramaters=params)
    for record in totalRCC11Relations_mm:
        totalRelations_mm =record['totalNoOfRCC11Relations_mm']
    return totalRelations_mm

def getTotalRelations_rcc11_sm():
    params = {}
    session = driver.session()
    query ="""
       match (nm:Map)
        where nm.map_type = "sketch_map"
       
        with nm 
        match (nm)-[hpr:HAS_PARTIAL_REPRESENTATION]->(nq:QCN)-[hn:HAS_NODE]->
        (nqn:QCN_Node)-[sr:SPATIAL_RELATION]->(nqn1:QCN_Node)
        where
        nq.relation_set = "RCC11" 
        return count(sr) As totalNoOfRCC11Relations
        """
    totalRCC11Relations= session.run (query, paramaters=params)
    for record in totalRCC11Relations:
        totalRelations =record['totalNoOfRCC11Relations']
    
    return totalRelations

def getCorrrctRelation_rcc11():
    params = {}
    session = driver.session()
    query ="""
        match (nm:Map),(nm_b:Map)
        where nm.map_type = "sketch_map"
        and nm_b.map_type = "metric_map"
        with nm, nm_b
        match (nm)-[hpr:HAS_PARTIAL_REPRESENTATION]->(nq:QCN)-[hn:HAS_NODE]->
        (nqn:QCN_Node)-[sr:SPATIAL_RELATION]->(nqn1:QCN_Node)
        with nm_b,nm,hn,nqn,nq,nqn1,sr
        match (nm_b)-[hpr_b:HAS_PARTIAL_REPRESENTATION]->
        (nq_b:QCN)-[hn_b:HAS_NODE]->(nqn_b:QCN_Node)-[sr_b:SPATIAL_RELATION]->(nqn1_b:QCN_Node)
        where
        nq.relation_set = "RCC11" and
        nq_b.relation_set = "RCC11" and
        nq.relation_set = nq_b.relation_set and
        sr.relation = sr_b.relation and
        nqn.feature_id = nqn_b.feature_id and
        nqn1.feature_id = nqn1_b.feature_id and
        nqn.geometry_type = nqn_b.geometry_type and
        nqn1.geometry_type = nqn1_b.geometry_type and 
        nqn.feat_type = nqn_b.feat_type and
        nqn1.feat_type = nqn1_b.feat_type
        return  count (sr.relation = sr_b.relation) As noOfCorrectRCC11Relations
        """
    matchedRCC11Relations= session.run (query, paramaters=params)
    for record in matchedRCC11Relations:
        matchedRelations =record['noOfCorrectRCC11Relations']
           
    return matchedRelations

def getWrongRelations_rcc11():
    params = {}
    session = driver.session()
    query ="""
        match (nm:Map),(nm_b:Map)
        where nm.map_type = "sketch_map"
        and nm_b.map_type = "metric_map"
        with nm, nm_b
        match (nm)-[hpr:HAS_PARTIAL_REPRESENTATION]->(nq:QCN)-[hn:HAS_NODE]->
        (nqn:QCN_Node)-[sr:SPATIAL_RELATION]->(nqn1:QCN_Node)
        with nm_b,nm,hn,nqn,nq,nqn1,sr
        
        match (nm_b)-[hpr_b:HAS_PARTIAL_REPRESENTATION]->
        (nq_b:QCN)-[hn_b:HAS_NODE]->(nqn_b:QCN_Node)-[sr_b:SPATIAL_RELATION]->(nqn1_b:QCN_Node)
        where
        nq.relation_set = "RCC11" and
        nq_b.relation_set = "RCC11" and
        
        nq.relation_set = nq_b.relation_set and
        not( sr.relation = sr_b.relation) and
        nqn.feature_id = nqn_b.feature_id and
        nqn1.feature_id = nqn1_b.feature_id and
        nqn.geometry_type = nqn_b.geometry_type and
        nqn1.geometry_type = nqn1_b.geometry_type and 
        nqn.feat_type = nqn_b.feat_type and
        nqn1.feat_type = nqn1_b.feat_type
        
        	return  count (sr.relation = sr_b.relation) As no_of_wrong_matched_RCC11_Relations
        """
    wrong_matched_RCC11_rels= session.run (query, paramaters=params)
    for record in wrong_matched_RCC11_rels:
        wrong_matched_rcc11 =record['no_of_wrong_matched_RCC11_Relations']
    return wrong_matched_rcc11 

###############################################Linear Ordering of Landmarks ############################################
def getTotalLinearOrderingReltions_mm():
    params = {}
    session = driver.session()
    query ="""
       match (nm:Map)
        where nm.map_type = "metric_map"
       
        with nm 
        match (nm)-[hpr:HAS_PARTIAL_REPRESENTATION]->(nq:QCN)-[hn:HAS_NODE]->
        (nqn:QCN_Node)-[sr:SPATIAL_RELATION]->(nqn1:QCN_Node)
        where
        nq.relation_set = "linearOrdering" 
        return count(sr) As totalNoOfLinearOrderingRelations_mm
        """
    totaLinearOrderingRelations_mm= session.run (query, paramaters=params)
    for record in totaLinearOrderingRelations_mm:
        total_LO_relation_mm =record['totalNoOfLinearOrderingRelations_mm']
    return total_LO_relation_mm


def getTotalLinearOrderingReltions_sm():
    params = {}
    session = driver.session()
    query ="""
       match (nm:Map)
        where nm.map_type = "sketch_map"
       
        with nm 
        match (nm)-[hpr:HAS_PARTIAL_REPRESENTATION]->(nq:QCN)-[hn:HAS_NODE]->
        (nqn:QCN_Node)-[sr:SPATIAL_RELATION]->(nqn1:QCN_Node)
        where
        nq.relation_set = "linearOrdering" 
        return count(sr) As totalNoOfLinearOrderingRelations
        """
    totaLinearOrderingRelations= session.run (query, paramaters=params)
    for record in totaLinearOrderingRelations:
        total_LO_relation =record['totalNoOfLinearOrderingRelations']
    return total_LO_relation

def getCorrectRelation_linearOrdering():
    params = {}
    session = driver.session()
    query ="""
       match (nm:Map),(nm_b:Map)
        where nm.map_type = "sketch_map"
        and nm_b.map_type = "metric_map"
        with nm, nm_b
        match (nm)-[hpr:HAS_PARTIAL_REPRESENTATION]->(nq:QCN)-[hn:HAS_NODE]->
        (nqn:QCN_Node)-[sr:SPATIAL_RELATION]->(nqn1:QCN_Node)
        with nm_b,nm,hn,nqn,nq,nqn1,sr
        
        match (nm_b)-[hpr_b:HAS_PARTIAL_REPRESENTATION]->
        (nq_b:QCN)-[hn_b:HAS_NODE]->(nqn_b:QCN_Node)-[sr_b:SPATIAL_RELATION]->(nqn1_b:QCN_Node)
        where
        nq.relation_set = "linearOrdering" and
        nq_b.relation_set = "linearOrdering" and
        
        nq.relation_set = nq_b.relation_set and
       
        nqn.feature_id = nqn_b.feature_id and
      	 sr.relation = sr_b.relation AND 
        nqn1.feature_id = nqn1_b.feature_id and
        nqn.geometry_type = nqn_b.geometry_type and
        nqn1.geometry_type = nqn1_b.geometry_type and 
        nqn.feat_type = nqn_b.feat_type and
        nqn1.feat_type = nqn1_b.feat_type
        return COUNT(sr.relation = sr_b.relation) As noOfCorrectLORelations
        """
    matched_LO_relations= session.run (query, paramaters=params)
    for record in matched_LO_relations:
        correct_LO_relation =record['noOfCorrectLORelations']
    
    return correct_LO_relation

def getWrongRelations_linearOrdering():
    params = {}
    session = driver.session()
    query ="""
       match (nm:Map),(nm_b:Map)
        where nm.map_type = "sketch_map"
        and nm_b.map_type = "metric_map"
        with nm, nm_b
        match (nm)-[hpr:HAS_PARTIAL_REPRESENTATION]->(nq:QCN)-[hn:HAS_NODE]->
        (nqn:QCN_Node)-[sr:SPATIAL_RELATION]->(nqn1:QCN_Node)
        with nm_b,nm,hn,nqn,nq,nqn1,sr
        
        match (nm_b)-[hpr_b:HAS_PARTIAL_REPRESENTATION]->
        (nq_b:QCN)-[hn_b:HAS_NODE]->(nqn_b:QCN_Node)-[sr_b:SPATIAL_RELATION]->(nqn1_b:QCN_Node)
        where
        nq.relation_set = "linearOrdering" and
        nq_b.relation_set = "linearOrdering" and
        
        nq.relation_set = nq_b.relation_set and
       
        nqn.feature_id = nqn_b.feature_id and
      	 not(sr.relation = sr_b.relation) AND 
        nqn1.feature_id = nqn1_b.feature_id and
        nqn.geometry_type = nqn_b.geometry_type and
        nqn1.geometry_type = nqn1_b.geometry_type and
        nqn.feat_type = nqn_b.feat_type and
        nqn1.feat_type = nqn1_b.feat_type
        
        	return COUNT(sr.relation = sr_b.relation) As no_of_wrong_matched_LO_rels
        """
    wrong_matched_LO_rels= session.run (query, paramaters=params)
    for record in wrong_matched_LO_rels:
        wrong_matched_LO =record['no_of_wrong_matched_LO_rels']
    
    return wrong_matched_LO

###################################### get LeftRight Accuracy#########################################################
def getTotalLeftRightRelations_mm():
    params = {}
    session = driver.session()
    query ="""
        match (nm:Map)
        where nm.map_type = "metric_map"
       
        with nm 
        match (nm)-[hpr:HAS_PARTIAL_REPRESENTATION]->(nq:QCN)-[hn:HAS_NODE]->
        (nqn:QCN_Node)-[sr:SPATIAL_RELATION]->(nqn1:QCN_Node)
        where
        nq.relation_set = "leftRight" and
        not (sr.relation ="nonAdjacent") 
        return count (sr) As total_noOf_LR_rels_mm
        """
    totalLeftRightRels_mm = session.run (query, paramaters=params)
    for record in totalLeftRightRels_mm:
        totalLeftRight_mm =record['total_noOf_LR_rels_mm']
    
    return totalLeftRight_mm

def getTotalLeftRightRelations_sm():
    params = {}
    session = driver.session()
    query ="""
        match (nm:Map)
        where nm.map_type = "sketch_map"
       
        with nm 
        match (nm)-[hpr:HAS_PARTIAL_REPRESENTATION]->(nq:QCN)-[hn:HAS_NODE]->
        (nqn:QCN_Node)-[sr:SPATIAL_RELATION]->(nqn1:QCN_Node)
        where
        nq.relation_set = "leftRight" and
        not (sr.relation ="nonAdjacent") 
        return count (sr) As total_noOf_LR_rels_sm
        """
    totalLeftRightRels_sm = session.run (query, paramaters=params)
    for record in totalLeftRightRels_sm:
        totalLeftRight_sm =record['total_noOf_LR_rels_sm']
    
    return totalLeftRight_sm

def getCorrectrelations_leftRight():
    params = {}
    session = driver.session()
    query ="""
      match (nm:Map),(nm_b:Map)
        where nm.map_type = "sketch_map"
        and nm_b.map_type = "metric_map"
        with nm, nm_b
        match (nm)-[hpr:HAS_PARTIAL_REPRESENTATION]->(nq:QCN)-[hn:HAS_NODE]->
        (nqn:QCN_Node)-[sr:SPATIAL_RELATION]->(nqn1:QCN_Node)
        with nm_b,nm,hn,nqn,nq,nqn1,sr
        
        match (nm_b)-[hpr_b:HAS_PARTIAL_REPRESENTATION]->
        (nq_b:QCN)-[hn_b:HAS_NODE]->(nqn_b:QCN_Node)-[sr_b:SPATIAL_RELATION]->(nqn1_b:QCN_Node)
        where
        nq.relation_set = "leftRight" and
        nq_b.relation_set = "leftRight" and
        
        nq.relation_set = nq_b.relation_set and
       
        nqn.feature_id = nqn_b.feature_id and
        sr.relation = sr_b.relation AND 
        not (sr.relation ="nonAdjacent") and
        not (sr_b.relation ="nonAdjacent") and
        nqn1.feature_id = nqn1_b.feature_id and
        nqn.geometry_type = nqn_b.geometry_type and
        nqn1.geometry_type = nqn1_b.geometry_type 
        return count(sr.relation= sr_b.relation) As no_of_matched_LR_rels
        """
    matched_LR_rels= session.run (query, paramaters=params)
    for record in matched_LR_rels:
        correct_LR_rels =record['no_of_matched_LR_rels']
    return correct_LR_rels

def getWrongCorrectrelations_leftRight():
    params = {}
    session = driver.session()
    query ="""
        match (nm:Map),(nm_b:Map)
        where nm.map_type = "sketch_map"
        and nm_b.map_type = "metric_map"
        with nm, nm_b
        match (nm)-[hpr:HAS_PARTIAL_REPRESENTATION]->(nq:QCN)-[hn:HAS_NODE]->
        (nqn:QCN_Node)-[sr:SPATIAL_RELATION]->(nqn1:QCN_Node)
        with nm_b,nm,hn,nqn,nq,nqn1,sr
        
        match (nm_b)-[hpr_b:HAS_PARTIAL_REPRESENTATION]->
        (nq_b:QCN)-[hn_b:HAS_NODE]->(nqn_b:QCN_Node)-[sr_b:SPATIAL_RELATION]->(nqn1_b:QCN_Node)
        where
        nq.relation_set = "leftRight" and
        nq_b.relation_set = "leftRight" and
        
        nq.relation_set = nq_b.relation_set and
       
        nqn.feature_id = nqn_b.feature_id and
        not(sr.relation = sr_b.relation) AND 
        not (sr.relation ="nonAdjacent") and
        not (sr_b.relation ="nonAdjacent") and
        nqn1.feature_id = nqn1_b.feature_id and
        nqn.geometry_type = nqn_b.geometry_type and
        nqn1.geometry_type = nqn1_b.geometry_type 
        return count(sr.relation= sr_b.relation) As no_of_wrong_matched_LR_rels
        """
    wrong_matched_LR_rels= session.run (query, paramaters=params)
    for record in wrong_matched_LR_rels:
        wrong_matched_LR =record['no_of_wrong_matched_LR_rels']
    return wrong_matched_LR

########################################################DE9IM##############################################################
def getTotalDE9IMRelations_mm():
    params = {}
    session = driver.session()
    query ="""
       match (nm:Map)
        where nm.map_type = "metric_map"
       
        with nm 
        match (nm)-[hpr:HAS_PARTIAL_REPRESENTATION]->(nq:QCN)-[hn:HAS_NODE]->
        (nqn:QCN_Node)-[sr:SPATIAL_RELATION]->(nqn1:QCN_Node)
        where
        nq.relation_set = "DE9IM" 
        return count(sr) As no_of_DE9IM_relation_streets_mm
        """
    total_DE9IM_relations_mm= session.run (query, paramaters=params)
    for record in total_DE9IM_relations_mm:
        total_DE9IM_rels_mm =record['no_of_DE9IM_relation_streets_mm']
        
    return total_DE9IM_rels_mm

def getTotalDE9IMRelations_sm():
    params = {}
    session = driver.session()
    query ="""
       match (nm:Map)
        where nm.map_type = "sketch_map"
       
        with nm 
        match (nm)-[hpr:HAS_PARTIAL_REPRESENTATION]->(nq:QCN)-[hn:HAS_NODE]->
        (nqn:QCN_Node)-[sr:SPATIAL_RELATION]->(nqn1:QCN_Node)
        where
        nq.relation_set = "DE9IM" 
        return count(sr) As no_of_DE9IM_relation_streets_sm
        """
    total_DE9IM_relations_sm= session.run (query, paramaters=params)
    for record in total_DE9IM_relations_sm:
        total_DE9IM_rels_sm =record['no_of_DE9IM_relation_streets_sm']
        
    return total_DE9IM_rels_sm

def getCorrectrelations_DE9IM():
    params = {}
    session = driver.session()
    query ="""
        match (nm:Map),(nm_b:Map)
        where nm.map_type = "sketch_map"
        and nm_b.map_type = "metric_map"
        with nm, nm_b
        match (nm)-[hpr:HAS_PARTIAL_REPRESENTATION]->(nq:QCN)-[hn:HAS_NODE]->
        (nqn:QCN_Node)-[sr:SPATIAL_RELATION]->(nqn1:QCN_Node)
        with nm_b,nm,hn,nqn,nq,nqn1,sr
        
        match (nm_b)-[hpr_b:HAS_PARTIAL_REPRESENTATION]->
        (nq_b:QCN)-[hn_b:HAS_NODE]->(nqn_b:QCN_Node)-[sr_b:SPATIAL_RELATION]->(nqn1_b:QCN_Node)
        where
        nq.relation_set = "DE9IM" and
        nq_b.relation_set = "DE9IM" and
        
        nq.relation_set = nq_b.relation_set and
       
        nqn.feature_id = nqn_b.feature_id and
        sr.relation = sr_b.relation AND 
        nqn1.feature_id = nqn1_b.feature_id and
        nqn.geometry_type = nqn_b.geometry_type and
        nqn1.geometry_type = nqn1_b.geometry_type 

        return count(sr.relation= sr_b.relation) As no_of_matched_DE9IM_rels
        """
    matched_DE9IM_rels= session.run (query, paramaters=params)
    for record in matched_DE9IM_rels:
        correct_DE9IM_rels =record['no_of_matched_DE9IM_rels']
    return correct_DE9IM_rels
 
    
def getWrongCorrectrelations_DE9IM():
    params = {}
    session = driver.session()
    query ="""
        match (nm:Map),(nm_b:Map)
        where nm.map_type = "sketch_map"
        and nm_b.map_type = "metric_map"
        with nm, nm_b
        match (nm)-[hpr:HAS_PARTIAL_REPRESENTATION]->(nq:QCN)-[hn:HAS_NODE]->
        (nqn:QCN_Node)-[sr:SPATIAL_RELATION]->(nqn1:QCN_Node)
        with nm_b,nm,hn,nqn,nq,nqn1,sr
        
        match (nm_b)-[hpr_b:HAS_PARTIAL_REPRESENTATION]->
        (nq_b:QCN)-[hn_b:HAS_NODE]->(nqn_b:QCN_Node)-[sr_b:SPATIAL_RELATION]->(nqn1_b:QCN_Node)
        where
        nq.relation_set = "DE9IM" and
        nq_b.relation_set = "DE9IM" and
        
        nq.relation_set = nq_b.relation_set and
       
        nqn.feature_id = nqn_b.feature_id and
        not(sr.relation = sr_b.relation) AND 
        nqn1.feature_id = nqn1_b.feature_id and
        nqn.geometry_type = nqn_b.geometry_type and
        nqn1.geometry_type = nqn1_b.geometry_type 

        return count(sr.relation= sr_b.relation) As no_of_wrong_matched_DE9IM_rels
        """
    wrong_matched_DE9IM_rels= session.run (query, paramaters=params)
    for record in wrong_matched_DE9IM_rels:
        wrong_matched_DE9IM =record['no_of_wrong_matched_DE9IM_rels']
    return wrong_matched_DE9IM
    
  ###################################################### Street Topological Relations ###############################################  

def getTotalStreetTopology_mm():
    params = {}
    session = driver.session()
    query ="""
       match (nm:Map)
        where nm.map_type = "metric_map"
       
        with nm 
        match (nm)-[hpr:HAS_PARTIAL_REPRESENTATION]->(nq:QCN)-[hn:HAS_NODE]->
        (nqn:QCN_Node)-[sr:SPATIAL_RELATION]->(nqn1:QCN_Node)
        where
        nq.relation_set = "streetTopology" 
        return count(sr) As no_of_topological_relation_streets_mm
        """
    total_street_topology_relations_mm= session.run (query, paramaters=params)
    for record in total_street_topology_relations_mm:
        total_top_streets_relation_mm =record['no_of_topological_relation_streets_mm']
    return total_top_streets_relation_mm
    
def getTotalStreetTopology_sm():
    params = {}
    session = driver.session()
    query ="""
       match (nm:Map)
        where nm.map_type = "sketch_map"
       
        with nm 
        match (nm)-[hpr:HAS_PARTIAL_REPRESENTATION]->(nq:QCN)-[hn:HAS_NODE]->
        (nqn:QCN_Node)-[sr:SPATIAL_RELATION]->(nqn1:QCN_Node)
        where
        nq.relation_set = "streetTopology" 
        return count(sr) As no_of_topological_relation_streets_sm
        """
    total_street_topology_relations_sm= session.run (query, paramaters=params)
    for record in total_street_topology_relations_sm:
        total_top_streets_relation_sm =record['no_of_topological_relation_streets_sm']
    return total_top_streets_relation_sm


def getCorrectrelations_streetTopology():
    params = {}
    session = driver.session()
    query ="""
      match (nm:Map),(nm_b:Map)
        where nm.map_type = "sketch_map"
        and nm_b.map_type = "metric_map"
        with nm, nm_b
        match (nm)-[hpr:HAS_PARTIAL_REPRESENTATION]->(nq:QCN)-[hn:HAS_NODE]->
        (nqn:QCN_Node)-[sr:SPATIAL_RELATION]->(nqn1:QCN_Node)
        with nm_b,nm,hn,nqn,nq,nqn1,sr
        
        match (nm_b)-[hpr_b:HAS_PARTIAL_REPRESENTATION]->
        (nq_b:QCN)-[hn_b:HAS_NODE]->(nqn_b:QCN_Node)-[sr_b:SPATIAL_RELATION]->(nqn1_b:QCN_Node)
        where
        nq.relation_set = "streetTopology" and
        nq_b.relation_set = "streetTopology" and
        
        nq.relation_set = nq_b.relation_set and
       
        nqn.feature_id = nqn_b.feature_id and
        sr.relation = sr_b.relation AND 
        nqn1.feature_id = nqn1_b.feature_id and
        nqn.geometry_type = nqn_b.geometry_type and
        nqn1.geometry_type = nqn1_b.geometry_type 
        return count(sr.relation= sr_b.relation) As no_of_matched_streetTop_rels
        """
    matched_streetTop_rels= session.run (query, paramaters=params)
    for record in matched_streetTop_rels:
        correct_streetTop_rels =record['no_of_matched_streetTop_rels']
    return correct_streetTop_rels


def getWrongCorrectrelations_streetTopology():
    params = {}
    session = driver.session()
    query ="""
        match (nm:Map),(nm_b:Map)
        where nm.map_type = "sketch_map"
        and nm_b.map_type = "metric_map"
        with nm, nm_b
        match (nm)-[hpr:HAS_PARTIAL_REPRESENTATION]->(nq:QCN)-[hn:HAS_NODE]->
        (nqn:QCN_Node)-[sr:SPATIAL_RELATION]->(nqn1:QCN_Node)
        with nm_b,nm,hn,nqn,nq,nqn1,sr
        
        match (nm_b)-[hpr_b:HAS_PARTIAL_REPRESENTATION]->
        (nq_b:QCN)-[hn_b:HAS_NODE]->(nqn_b:QCN_Node)-[sr_b:SPATIAL_RELATION]->(nqn1_b:QCN_Node)
        where
        nq.relation_set = "streetTopology" and
        nq_b.relation_set = "streetTopology" and
        
        nq.relation_set = nq_b.relation_set and
       
        nqn.feature_id = nqn_b.feature_id and
        not(sr.relation = sr_b.relation) and 
        nqn1.feature_id = nqn1_b.feature_id and
        nqn.geometry_type = nqn_b.geometry_type and
        nqn1.geometry_type = nqn1_b.geometry_type 

        return count(sr.relation= sr_b.relation) As no_of_wrong_matched_streetTop_rels
        """
    wrong_matched_streetTop_rels= session.run (query, paramaters=params)
    for record in wrong_matched_streetTop_rels:
        wrong_matched_streetTop =record['no_of_wrong_matched_streetTop_rels']
    return wrong_matched_streetTop


############################################### OPRA relation matching ############################
    
def getTotalOPRA_mm():
    params = {}
    session = driver.session()
    query ="""
       match (nm:Map)
        where nm.map_type = "metric_map"
       
        with nm 
        match (nm)-[hpr:HAS_PARTIAL_REPRESENTATION]->(nq:QCN)-[hn:HAS_NODE]->
        (nqn:QCN_Node)-[sr:SPATIAL_RELATION]->(nqn1:QCN_Node)
        where
        nq.relation_set = "opra" and 
        not (sr.relation ="nonAdjacent") 
        return count(sr) As no_of_opra_relation_streets_mm
        """
    total_opra_relations_mm= session.run (query, paramaters=params)
    for record in total_opra_relations_mm:
        total_opra_streets_relation_mm =record['no_of_opra_relation_streets_mm']
    return total_opra_streets_relation_mm
    

def getTotalOPRA_sm():
    params = {}
    session = driver.session()
    query ="""
       match (nm:Map)
        where nm.map_type = "sketch_map"
       
        with nm 
        match (nm)-[hpr:HAS_PARTIAL_REPRESENTATION]->(nq:QCN)-[hn:HAS_NODE]->
        (nqn:QCN_Node)-[sr:SPATIAL_RELATION]->(nqn1:QCN_Node)
        where
        nq.relation_set = "opra" and 
        not (sr.relation ="nonAdjacent") 
        return count(sr) As no_of_opra_relation_streets_sm
        """
    total_opra_relations_sm= session.run (query, paramaters=params)
    for record in total_opra_relations_sm:
        total_opra_streets_relation_sm =record['no_of_opra_relation_streets_sm']
    return total_opra_streets_relation_sm

def getCorrectrelations_opra():
    params = {}
    session = driver.session()
    query ="""
     match (nm:Map),(nm_b:Map)
        where nm.map_type = "sketch_map"
        and nm_b.map_type = "metric_map"
        with nm, nm_b
        match (nm)-[hpr:HAS_PARTIAL_REPRESENTATION]->(nq:QCN)-[hn:HAS_NODE]->
        (nqn:QCN_Node)-[sr:SPATIAL_RELATION]->(nqn1:QCN_Node)
        with nm_b,nm,hn,nqn,nq,nqn1,sr
        
        match (nm_b)-[hpr_b:HAS_PARTIAL_REPRESENTATION]->
        (nq_b:QCN)-[hn_b:HAS_NODE]->(nqn_b:QCN_Node)-[sr_b:SPATIAL_RELATION]->(nqn1_b:QCN_Node)
        where
        nq.relation_set = "opra" and
        nq_b.relation_set = "opra" and
        
        nq.relation_set = nq_b.relation_set and
       
        nqn.feature_id = nqn_b.feature_id and
        sr.relation = sr_b.relation AND 
        not (sr.relation ="nonAdjacent") and
        not (sr_b.relation ="nonAdjacent") and
        nqn1.feature_id = nqn1_b.feature_id and
        nqn.geometry_type = nqn_b.geometry_type and
        nqn1.geometry_type = nqn1_b.geometry_type 

        return count(sr.relation= sr_b.relation) As no_of_matched_OPRA_rels
        """
    matched_opra_rels= session.run (query, paramaters=params)
    for record in matched_opra_rels:
        correct_opra_rels =record['no_of_matched_OPRA_rels']
    return correct_opra_rels

def getWrongCorrectrelations_opra():
    params = {}
    session = driver.session()
    query ="""
        match (nm:Map),(nm_b:Map)
        where nm.map_type = "sketch_map"
        and nm_b.map_type = "metric_map"
        with nm, nm_b
        match (nm)-[hpr:HAS_PARTIAL_REPRESENTATION]->(nq:QCN)-[hn:HAS_NODE]->
        (nqn:QCN_Node)-[sr:SPATIAL_RELATION]->(nqn1:QCN_Node)
        with nm_b,nm,hn,nqn,nq,nqn1,sr
        
        match (nm_b)-[hpr_b:HAS_PARTIAL_REPRESENTATION]->
        (nq_b:QCN)-[hn_b:HAS_NODE]->(nqn_b:QCN_Node)-[sr_b:SPATIAL_RELATION]->(nqn1_b:QCN_Node)
        where
        nq.relation_set = "opra" and
        nq_b.relation_set = "opra" and
        
        nq.relation_set = nq_b.relation_set and
       
        nqn.feature_id = nqn_b.feature_id and
        not(sr.relation = sr_b.relation) AND 
        not (sr.relation ="nonAdjacent") and
        not (sr_b.relation ="nonAdjacent") and
        nqn1.feature_id = nqn1_b.feature_id and
        nqn.geometry_type = nqn_b.geometry_type and
        nqn1.geometry_type = nqn1_b.geometry_type 
        
        return count(sr.relation= sr_b.relation) As no_of_wrong_matched_OPRA_rels
        """
    wrong_matched_opra_rels= session.run (query, paramaters=params)
    for record in wrong_matched_opra_rels:
        wrong_matched_opra =record['no_of_wrong_matched_OPRA_rels']
    return wrong_matched_opra
    
###################################################### 






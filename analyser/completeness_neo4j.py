# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 13:53:12 2018

@author: s_jan001
"""

"""
Created on Fri Mar 23 11:45:06 2018

@author: s_jan001
"""
from neo4j.v1 import GraphDatabase


uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri)

# to delete records from database
def deleteAllRecords():
    params = {}
    session = driver.session()
    deleted = """
        match(N) DETACH DELETE(N)
        """
    
    session.run (deleted, paramaters=params )
    return "Deleted"


def createGraphStructure():
    params = {}
    session = driver.session()
    structure = """
            create (s:SmartSkeMaRoot {name:"sketch map data root"})-[rhm:HAS_MAPS]->(mr:MapsRoot {name:"maps"})
            merge (s)-[rhr:HAS_RELATION_SETS]->(rs:RelationSetRoot {name:"relation_sets"})
            merge (mr)-[rhmc1:HAS_MAP_CLASS]->(pmm:metric_maps {map_class:"metric_maps"})
            merge (mr)-[rhmc2:HAS_MAP_CLASS]->(psm:sketch_maps {map_class:"sketch_maps"})
            merge (rs)-[rhrc1:HAS_RELATION_SET_CLASS]->(rt1:RelationType {name:"RegionStarVars"})
            merge (rs)-[rhrc2:HAS_RELATION_SET_CLASS]->(rt2:RelationType {name:"DE9IM"})
            merge (rs)-[rhrc3:HAS_RELATION_SET_CLASS]->(rt3:RelationType {name:"leftRight"})
            merge (rs)-[rhrc4:HAS_RELATION_SET_CLASS]->(rt4:RelationType {name:"RCC11"})
            merge (rs)-[rhrc5:HAS_RELATION_SET_CLASS]->(rt5:RelationType {name:"opra"})
            merge (rs)-[rhrc6:HAS_RELATION_SET_CLASS]->(rt6:RelationType {name:"relDist"})
            merge (rs)-[rhrc7:HAS_RELATION_SET_CLASS]->(rt7:RelationType {name:"linearOrdering"})
            merge (rs)-[rhrc8:HAS_RELATION_SET_CLASS]->(rt8:RelationType {name:"streetTopology"})
            return s,mr,pmm,psm,rs,rt1,rt2,rt3,rt4,rt5,rt6,rt7,rt8
        """
    
    session.run (structure, paramaters=params )
    return "Database is successfully initialized...!"    



def get_landmarks_MM():
    params = {}
    session = driver.session()
    count_mm_Landmarks_query = """
        match(sm:Map)-[fn:HAS_FEATURE]->(f:Feature_Node) 
        where sm.map_type = "metric_map"
        with f 
        where
        f.geometry_type="Polygon" and
        f.feat_type = "Landmark"
        return COUNT (f) AS no_of_mm_landmarks
        """
    
    total_mm_landmarks = session.run (count_mm_Landmarks_query, paramaters=params )
    for record in total_mm_landmarks:
        results =record['no_of_mm_landmarks']
       
    return results

def get_streets_mm():
    params = {}
    session = driver.session()
    count_mm_Streets_query = """
        match(sm:Map)-[fn:HAS_FEATURE]->(f:Feature_Node) 
        where sm.map_type = "metric_map"
        with f 
        where
        f.geometry_type="LineString"
        return COUNT (f) AS no_of_mm_streets
        """
    
    total_mm_Streets = session.run (count_mm_Streets_query, paramaters=params )
    for record in total_mm_Streets:
        results =record['no_of_mm_streets']
        
    return results


def get_cityblocks_mm():
    params = {}
    session = driver.session()
    count_mm_Cityblocks_query = """
        match(sm:Map)-[fn:HAS_FEATURE]->(f:Feature_Node) 
        where sm.map_type = "metric_map"
        with f 
        where
        f.geometry_type="Polygon" and
        f.feat_type = "Cityblock"
        return COUNT (f) AS no_of_mm_cityblocks
        """
    
    total_mm_Cityblocks = session.run (count_mm_Cityblocks_query, paramaters=params )
    for record in total_mm_Cityblocks:
        results =record['no_of_mm_cityblocks']
       
    return results


def get_landmarks_sm():
    params = {}
    session = driver.session()
    countSketchLandmarks_query = """
        match(sm:Map)-[fn:HAS_FEATURE]->(f:Feature_Node) 
        where sm.map_type = "sketch_map"
        with f 
        where
        f.geometry_type="Polygon" and
        f.feat_type = "Landmark"
        return COUNT (f) AS no_of_sketched_landmarks
        """
    
    totalSketchedlandmarks = session.run (countSketchLandmarks_query, paramaters=params )
    for record in totalSketchedlandmarks:
        results =record['no_of_sketched_landmarks']
       
    return results

def get_streets_sm():
    params = {}
    session = driver.session()
    countSketchStreets_query = """
        match(sm:Map)-[fn:HAS_FEATURE]->(f:Feature_Node) 
        where sm.map_type = "sketch_map"
        with f 
        where
        f.geometry_type="LineString"
        return COUNT (f) AS no_of_sketched_streets
        """
    
    totalSketchedStreets = session.run (countSketchStreets_query, paramaters=params )
    for record in totalSketchedStreets:
        results =record['no_of_sketched_streets']
       
    return results


def get_cityblocks_sm():
    params = {}
    session = driver.session()
    countSketchCityblocks_query = """
        match(sm:Map)-[fn:HAS_FEATURE]->(f:Feature_Node) 
        where sm.map_type = "sketch_map"
        with f 
        where
        f.geometry_type="Polygon" and
        f.feat_type = "Cityblock"
        return COUNT (f) AS no_of_sketched_cityblocks
        """
    
    totalSketchedCityblocks = session.run (countSketchCityblocks_query, paramaters=params )
    for record in totalSketchedCityblocks:
        results =record['no_of_sketched_cityblocks']
       
    return results

//-----------------------------------------------------------------------
// Manus VR Apollo network types to be public exposed
//-----------------------------------------------------------------------

#pragma once

#ifdef PUBLICTYPES_HPP
#define PUBLICTYPES_HPP

#ifdef __cplusplus
#include <cstdint>
#else
#include <stdint>
#endif

#if __cplusplus >= 201103L
constexpr uint32_t APOLLO_MIN_PACKET_BYTES = 8;
constexpr uint32_t APOLLO_MAX_PACKET_BYTES = 1024;
#endif

#ifdef __cplusplus
extern "C"
{
#endif 

enum apollo_dev_t
{
	DEVICES_INVALID = 0,
	DEVICES_DEBUG,
	DEVICES_REVD
};

enum apollo_source_t
{
	SOURCE_INVALID = 0,
	SOURCE_DEVICEDATA,
	SOURCE_FILTERED,
	SOURCE_FILTERED_DEFAULT
};

enum apollo_filter_t
{
	FILTER_NONE = 0,
	FILTER_COORDINATESYSTEMCONVERSION,
	FILTER_MESHMAPPING,
	FILTER_GESTURE
};

enum apollo_gesture_t
{
	GESTURE_NONE = 0,
	GESTURE_OPEN_HAND,
	GESTURE_FIST,
	GESTURE_INDEX_PINCH
};

enum apollo_laterality_t
{
	SIDE_LEFT = -1,
	SIDE_RIGHT = 1
};

enum coor_axis_t
{
	